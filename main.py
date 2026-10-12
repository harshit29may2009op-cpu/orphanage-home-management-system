"""Menu-driven Class 12 Python + MySQL orphanage-home project.

Use fictional records only. Admission decisions and policy checks require a human.
"""
from datetime import date
from decimal import Decimal, InvalidOperation

import mysql.connector

from charts import generate_charts
from config import connect_db


def ask(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("Please enter a value.")


def ask_date(prompt):
    while True:
        value = ask(prompt + " (YYYY-MM-DD): ")
        try:
            return date.fromisoformat(value)
        except ValueError:
            print("Use a valid date such as 2026-10-12.")


def ask_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(ask(prompt))
            if minimum is not None and value < minimum:
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except ValueError:
            print("Enter a whole number in the allowed range.")


def ask_amount(prompt):
    while True:
        try:
            value = Decimal(ask(prompt))
            if value <= 0:
                raise InvalidOperation
            return value
        except (InvalidOperation, ValueError):
            print("Enter an amount greater than zero.")


def choose_gender():
    options = ["Girl", "Boy", "Another identity", "Prefer not to say"]
    print("Gender is recorded for context and aggregate charts only.")
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")
    return options[ask_integer("Choose: ", 1, len(options)) - 1]


def dashboard(connection):
    cursor = connection.cursor()
    print("\n=== HOME DASHBOARD ===")
    for label, table in [
        ("Children in care", "children"),
        ("Admission applications", "admission_applications"),
        ("Donors", "donors"),
        ("Parents/guardians", "parents_guardians"),
        ("Active staff", "staff_members"),
        ("Inventory items", "inventory_items"),
    ]:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        print(f"{label}: {cursor.fetchone()[0]}")
    cursor.execute(
        "SELECT item_name, quantity_on_hand, reorder_level FROM inventory_items "
        "WHERE quantity_on_hand <= reorder_level ORDER BY item_name"
    )
    low_stock = cursor.fetchall()
    print("Low-stock items:")
    if low_stock:
        for name, quantity, reorder in low_stock:
            print(f"  {name}: {quantity} on hand (reorder at {reorder})")
    else:
        print("  None")
    cursor.close()


def add_child(connection):
    print("\nCreate a child profile only after an authorized human decision.")
    code = ask("Demo child code: ")
    name = ask("Display name (use fictional demo data): ")
    birth = ask_date("Date of birth")
    gender = choose_gender()
    admission = ask_date("Admission date")
    grade = ask("School grade: ", required=False)
    school = ask("School name: ", required=False)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO children "
        "(child_code, display_name, date_of_birth, gender, admission_date, school_grade, school_name) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (code, name, birth, gender, admission, grade or None, school or None),
    )
    connection.commit()
    print(f"Saved demo child profile with ID {cursor.lastrowid}.")
    cursor.close()


def search_children(connection):
    term = ask("Search by child code or display name (blank lists all): ", required=False)
    cursor = connection.cursor()
    if term:
        cursor.execute(
            "SELECT child_id, child_code, display_name, gender, care_status, school_grade "
            "FROM children WHERE child_code LIKE %s OR display_name LIKE %s "
            "ORDER BY child_id LIMIT 100",
            (f"%{term}%", f"%{term}%"),
        )
    else:
        cursor.execute(
            "SELECT child_id, child_code, display_name, gender, care_status, school_grade "
            "FROM children ORDER BY child_id LIMIT 100"
        )
    rows = cursor.fetchall()
    print("\nID | Code | Display name | Gender | Status | Grade")
    for row in rows:
        print(" | ".join(str(value or "-") for value in row))
    if not rows:
        print("No matching records.")
    cursor.close()


def create_application(connection):
    print("\nNew admission application. Use fictional demo information.")
    code = ask("Application code: ")
    applicant = ask("Applicant display name: ")
    age_text = ask("Age in years (leave blank if not recorded): ", required=False)
    age = int(age_text) if age_text else None
    if age is not None and not 0 <= age <= 120:
        print("Age must be between 0 and 120.")
        return
    gender = choose_gender()
    received = ask_date("Date received")
    source = ask("Referral source: ")
    parent_name = ask("Parent or guardian display name (fictional): ")
    relationship = ask("Relationship to applicant: ")
    contact_ref = ask("Contact reference (use DEMO ONLY; no real number): ")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO parents_guardians (display_name, contact_reference) "
        "VALUES (%s, %s)",
        (parent_name, contact_ref),
    )
    parent_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO admission_applications "
        "(application_code, applicant_display_name, age_years, gender, received_on, "
        "referral_source) VALUES (%s, %s, %s, %s, %s, %s)",
        (code, applicant, age, gender, received, source),
    )
    application_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO application_parent_links "
        "(application_id, parent_guardian_id, relationship_to_applicant) "
        "VALUES (%s, %s, %s)",
        (application_id, parent_id, relationship),
    )
    cursor.execute(
        "INSERT INTO application_reviews (application_id, criterion_id) "
        "SELECT %s, criterion_id FROM review_criteria WHERE is_active = TRUE",
        (application_id,),
    )
    connection.commit()
    print(f"Application {code} and separate parent/guardian record saved.")
    print("The system does not calculate eligibility or make placement decisions.")
    cursor.close()

def list_applications(connection):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT aa.application_id, aa.application_code, aa.applicant_display_name, "
        "aa.received_on, aa.status, pg.display_name, apl.relationship_to_applicant "
        "FROM admission_applications aa "
        "LEFT JOIN application_parent_links apl ON aa.application_id=apl.application_id "
        "LEFT JOIN parents_guardians pg ON apl.parent_guardian_id=pg.parent_guardian_id "
        "ORDER BY aa.received_on DESC LIMIT 100"
    )
    rows = cursor.fetchall()
    print("\nID | Code | Applicant | Received | Status | Parent/guardian | Relationship")
    for row in rows:
        print(" | ".join(str(value or "-") for value in row))
    if not rows:
        print("No applications yet.")
    cursor.close()


def review_application(connection):
    list_applications(connection)
    application_id = ask_integer("Application ID to review: ", 1)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT ar.review_id, rc.criterion_name, ar.review_status "
        "FROM application_reviews ar JOIN review_criteria rc "
        "ON rc.criterion_id = ar.criterion_id "
        "WHERE ar.application_id = %s ORDER BY rc.criterion_id",
        (application_id,),
    )
    rows = cursor.fetchall()
    if not rows:
        cursor.close()
        print("Application not found, or checklist is empty.")
        return
    print("\nChecklist:")
    for review_id, criterion, status in rows:
        print(f"  {review_id}. {criterion} — {status}")
    valid_review_ids = {row[0] for row in rows}
    review_id = ask_integer("Checklist item ID to update: ", 1)
    if review_id not in valid_review_ids:
        cursor.close()
        print("That checklist item does not belong to this application.")
        return
    status_options = ["Not started", "In review", "Reviewed"]
    for number, option in enumerate(status_options, start=1):
        print(f"  {number}. {option}")
    status = status_options[ask_integer("New checklist status: ", 1, 3) - 1]
    reviewer = ask("Reviewer display name (demo): ")
    cursor.execute(
        "UPDATE application_reviews SET review_status=%s, reviewer_name=%s, "
        "reviewed_on=%s WHERE review_id=%s AND application_id=%s",
        (status, reviewer, date.today() if status == "Reviewed" else None,
         review_id, application_id),
    )
    connection.commit()
    print("Checklist updated. It records review progress, not an eligibility result.")
    decision = ask(
        "Record a human decision now? (leave blank to keep current status): ",
        required=False,
    ).lower()
    if decision in {"y", "yes"}:
        choices = ["Pending review", "Approved by reviewer", "Referred", "Closed"]
        for number, option in enumerate(choices, start=1):
            print(f"  {number}. {option}")
        new_status = choices[ask_integer("Human decision status: ", 1, 4) - 1]
        note = ask("Short non-sensitive note: ", required=False)
        cursor.execute(
            "UPDATE admission_applications SET status=%s, reviewer_name=%s, "
            "reviewer_note=%s, decision_on=%s WHERE application_id=%s",
            (new_status, reviewer, note or None,
             date.today() if new_status != "Pending review" else None, application_id),
        )
        connection.commit()
        print("Human-entered workflow status saved.")
    cursor.close()


def add_donor(connection):
    code = ask("Demo donor code: ")
    name = ask("Donor display name (fictional for this project): ")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO donors (donor_code, display_name, contact_reference) "
        "VALUES (%s, %s, %s)",
        (code, name, "DEMO ONLY"),
    )
    connection.commit()
    print(f"Donor saved with ID {cursor.lastrowid}.")
    cursor.close()


def record_donation(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT donor_id, donor_code, display_name FROM donors ORDER BY donor_id")
    donors = cursor.fetchall()
    for donor_id, code, name in donors:
        print(f"{donor_id}. {code} — {name}")
    if not donors:
        cursor.close()
        print("Add a donor first.")
        return
    donor_id = ask_integer("Donor ID: ", 1)
    donated_on = ask_date("Donation date")
    amount = ask_amount("Amount: ")
    purpose = ask("Purpose: ")
    method = ask("Payment method: ")
    cursor.execute(
        "INSERT INTO donations (donor_id, donated_on, amount, purpose, payment_method) "
        "VALUES (%s, %s, %s, %s, %s)",
        (donor_id, donated_on, amount, purpose, method),
    )
    connection.commit()
    print("Donation recorded.")
    cursor.close()


def record_expense(connection):
    spent_on = ask_date("Expense date")
    category = ask("Category: ")
    amount = ask_amount("Amount: ")
    description = ask("Description (no sensitive details): ")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO expenses (spent_on, category, amount, description) "
        "VALUES (%s, %s, %s, %s)",
        (spent_on, category, amount, description),
    )
    connection.commit()
    print("Expense recorded.")
    cursor.close()


def add_education_record(connection):
    code = ask("Child code: ")
    academic_year = ask("Academic year (e.g. 2026-27): ")
    grade = ask("Grade: ")
    attendance = ask_amount("Attendance percent (use a value above 0): ")
    result = ask_amount("Result percent (use a value above 0): ")
    if attendance > 100 or result > 100:
        print("Percentages must not exceed 100.")
        return
    cursor = connection.cursor()
    cursor.execute("SELECT child_id FROM children WHERE child_code = %s", (code,))
    row = cursor.fetchone()
    if not row:
        cursor.close()
        print("Child code not found.")
        return
    cursor.execute(
        "INSERT INTO education_records "
        "(child_id, academic_year, school_grade, attendance_percent, result_percent) "
        "VALUES (%s, %s, %s, %s, %s)",
        (row[0], academic_year, grade, attendance, result),
    )
    connection.commit()
    print("Education record saved.")
    cursor.close()


def inventory_menu(connection):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT item_id, item_code, item_name, quantity_on_hand, reorder_level, unit_name "
        "FROM inventory_items ORDER BY item_id"
    )
    items = cursor.fetchall()
    print("\nID | Code | Item | On hand | Reorder at | Unit")
    for row in items:
        print(" | ".join(str(value) for value in row))
    if not items:
        cursor.close()
        print("No inventory items. Load demo data first.")
        return
    item_id = ask_integer("Item ID to adjust (0 to cancel): ", 0)
    if item_id == 0:
        connection.rollback()
        cursor.close()
        return
    cursor.execute(
        "SELECT quantity_on_hand FROM inventory_items WHERE item_id=%s FOR UPDATE",
        (item_id,),
    )
    row = cursor.fetchone()
    if not row:
        connection.rollback()
        cursor.close()
        print("Item not found.")
        return
    movement = ask("Movement type IN or OUT: ").upper()
    if movement not in {"IN", "OUT"}:
        connection.rollback()
        cursor.close()
        print("Choose IN or OUT.")
        return
    quantity = ask_integer("Quantity: ", 1)
    current = row[0]
    if movement == "OUT" and quantity > current:
        connection.rollback()
        cursor.close()
        print("There is not enough stock for that adjustment.")
        return
    purpose = ask("Reason: ")
    cursor.execute(
        "INSERT INTO inventory_movements "
        "(item_id, movement_type, quantity, moved_on, purpose) VALUES (%s, %s, %s, %s, %s)",
        (item_id, movement, quantity, date.today(), purpose),
    )
    updated = current + quantity if movement == "IN" else current - quantity
    cursor.execute(
        "UPDATE inventory_items SET quantity_on_hand=%s WHERE item_id=%s",
        (updated, item_id),
    )
    connection.commit()
    cursor.close()
    print("Inventory and movement log updated.")


def list_staff(connection):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT staff_id, staff_code, display_name, role_name, is_active "
        "FROM staff_members ORDER BY staff_id"
    )
    rows = cursor.fetchall()
    print("\nID | Code | Name | Role | Active")
    for row in rows:
        print(" | ".join(str(value) for value in row))
    if not rows:
        print("No staff records yet.")
    cursor.close()


def manage_staff(connection):
    while True:
        print("\nSTAFF MANAGEMENT: 1 Add  2 List  3 Update role/status  0 Back")
        choice = ask("Choose: ")
        if choice == "0":
            return
        if choice == "1":
            code = ask("Staff code: ")
            name = ask("Staff display name (fictional): ")
            role = ask("Role: ")
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO staff_members (staff_code, display_name, role_name) "
                "VALUES (%s, %s, %s)",
                (code, name, role),
            )
            connection.commit()
            print(f"Staff record added with ID {cursor.lastrowid}.")
            cursor.close()
        elif choice == "2":
            list_staff(connection)
        elif choice == "3":
            list_staff(connection)
            staff_id = ask_integer("Staff ID to update: ", 1)
            role = ask("New role: ")
            print("  1. Active")
            print("  2. Inactive")
            active = ask_integer("Choose status: ", 1, 2) == 1
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE staff_members SET role_name=%s, is_active=%s WHERE staff_id=%s",
                (role, active, staff_id),
            )
            connection.commit()
            print("Staff record updated." if cursor.rowcount else "Staff ID not found.")
            cursor.close()
        else:
            print("Choose a listed option.")


def add_parent_record(connection):
    name = ask("Parent/guardian display name (fictional): ")
    contact = ask("Contact reference (use DEMO ONLY; no real number): ")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO parents_guardians (display_name, contact_reference) "
        "VALUES (%s, %s)",
        (name, contact),
    )
    connection.commit()
    print(f"Separate parent/guardian record added with ID {cursor.lastrowid}.")
    cursor.close()


def list_parent_records(connection):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT pg.parent_guardian_id, pg.display_name, pg.contact_reference, "
        "ch.child_code, cpl.relationship_to_child, cpl.authority_review_status "
        "FROM parents_guardians pg "
        "LEFT JOIN child_parent_links cpl "
        "ON pg.parent_guardian_id=cpl.parent_guardian_id "
        "LEFT JOIN children ch ON cpl.child_id=ch.child_id "
        "ORDER BY pg.parent_guardian_id, ch.child_code"
    )
    rows = cursor.fetchall()
    print("\nID | Parent/guardian | Contact reference | Child code | Relationship | Review")
    for row in rows:
        print(" | ".join(str(value or "-") for value in row))
    if not rows:
        print("No parent/guardian records yet.")
    cursor.close()


def link_parent_to_child(connection):
    code = ask("Child code: ")
    cursor = connection.cursor()
    cursor.execute("SELECT child_id FROM children WHERE child_code=%s", (code,))
    child = cursor.fetchone()
    if not child:
        cursor.close()
        print("Child code not found.")
        return
    cursor.execute(
        "SELECT parent_guardian_id, display_name FROM parents_guardians "
        "ORDER BY parent_guardian_id"
    )
    parents = cursor.fetchall()
    for parent_id, name in parents:
        print(f"{parent_id}. {name}")
    if not parents:
        cursor.close()
        print("Add a parent/guardian record first.")
        return
    parent_id = ask_integer("Parent/guardian ID: ", 1)
    relation = ask("Relationship to child: ")
    statuses = ["Not reviewed", "Pending review", "Reviewed by authorized person"]
    for number, status in enumerate(statuses, start=1):
        print(f"  {number}. {status}")
    review_status = statuses[ask_integer("Authority-review status: ", 1, 3) - 1]
    cursor.execute(
        "INSERT INTO child_parent_links "
        "(child_id, parent_guardian_id, relationship_to_child, authority_review_status) "
        "VALUES (%s, %s, %s, %s)",
        (child[0], parent_id, relation, review_status),
    )
    connection.commit()
    cursor.close()
    print("Parent/guardian linked to the child.")


def manage_parents(connection):
    while True:
        print("\nPARENT/GUARDIAN RECORDS: 1 Add  2 List  3 Link to child  0 Back")
        choice = ask("Choose: ")
        if choice == "0":
            return
        if choice == "1":
            add_parent_record(connection)
        elif choice == "2":
            list_parent_records(connection)
        elif choice == "3":
            link_parent_to_child(connection)
        else:
            print("Choose a listed option.")


def main():
    print("=" * 64)
    print("ORPHANAGE HOME MANAGEMENT — CLASS 12 DEMONSTRATION")
    print("Use fictional data only. Do not enter real child or family details.")
    print("=" * 64)
    connection = connect_db()
    try:
        while True:
            print(
                "\n1 Dashboard  2 Add child profile  3 Search/list children"
                "\n4 Register admission application  5 List applications"
                "\n6 Review checklist / record human decision"
                "\n7 Add donor  8 Record donation  9 Record expense"
                "\n10 Add education record  11 Inventory  12 Generate charts"
                "\n13 Staff management  14 Parent/guardian records"
                "\n0 Exit"
            )
            choice = ask("Choose an option: ")
            try:
                if choice == "1":
                    dashboard(connection)
                elif choice == "2":
                    add_child(connection)
                elif choice == "3":
                    search_children(connection)
                elif choice == "4":
                    create_application(connection)
                elif choice == "5":
                    list_applications(connection)
                elif choice == "6":
                    review_application(connection)
                elif choice == "7":
                    add_donor(connection)
                elif choice == "8":
                    record_donation(connection)
                elif choice == "9":
                    record_expense(connection)
                elif choice == "10":
                    add_education_record(connection)
                elif choice == "11":
                    inventory_menu(connection)
                elif choice == "12":
                    for path in generate_charts(connection):
                        print(f"Created {path}")
                elif choice == "13":
                    manage_staff(connection)
                elif choice == "14":
                    manage_parents(connection)
                elif choice == "0":
                    break
                else:
                    print("Choose a listed option.")
            except (mysql.connector.Error, ValueError) as error:
                connection.rollback()
                print(f"Action could not be completed: {error}")
    finally:
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    try:
        main()
    except (mysql.connector.Error, RuntimeError) as error:
        print(f"Could not start the project: {error}")
        print("Check MySQL, the schema import, and your local .env settings.")
