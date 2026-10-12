# Orphanage Home Management System
# Class 12 Informatics Practices project

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from config import DB_CONFIG


def connect_database():
    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )


def get_rows(query, values=()):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(query, values)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def save_record(query, values=()):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print("Record saved successfully.")


def show_rows(rows):
    if len(rows) == 0:
        print("No records found.")
    else:
        for row in rows:
            print(row)


def view_children():
    query = "SELECT child_id, name, age, gender, school_class, admission_date, care_status, adoption_legal_status FROM children ORDER BY child_id"
    rows = get_rows(query)
    show_rows(rows)


def add_child():
    print("\nAdd a child record")
    name = input("Child name: ")
    age = int(input("Age: "))
    gender = input("Gender (optional): ")
    school_class = int(input("School class: "))
    admission_date = input("Admission date (YYYY-MM-DD): ")

    query = """INSERT INTO children
    (name, age, gender, school_class, admission_date)
    VALUES (%s, %s, %s, %s, %s)"""
    values = (name, age, gender, school_class, admission_date)
    save_record(query, values)


def view_guardians():
    query = "SELECT guardian_id, name, phone, address FROM guardians ORDER BY guardian_id"
    rows = get_rows(query)
    show_rows(rows)


def add_guardian():
    print("\nAdd a parent or guardian record")
    name = input("Parent/guardian name: ")
    phone = input("Contact number or demo contact: ")
    address = input("Address or area: ")

    query = "INSERT INTO guardians (name, phone, address) VALUES (%s, %s, %s)"
    values = (name, phone, address)
    save_record(query, values)


def link_guardian():
    print("\nLink a child with a parent or guardian")
    child_id = int(input("Child ID: "))
    guardian_id = int(input("Parent/guardian ID: "))
    relationship = input("Relationship to child: ")

    query = """INSERT INTO child_guardians
    (child_id, guardian_id, relationship)
    VALUES (%s, %s, %s)"""
    values = (child_id, guardian_id, relationship)
    save_record(query, values)


def view_child_guardians():
    query = """SELECT children.name, guardians.name, child_guardians.relationship,
    guardians.phone
    FROM child_guardians
    JOIN children ON child_guardians.child_id = children.child_id
    JOIN guardians ON child_guardians.guardian_id = guardians.guardian_id
    ORDER BY children.name"""
    rows = get_rows(query)
    show_rows(rows)


def view_applications():
    query = """SELECT applications.application_id, applications.applicant_name,
    applications.age, applications.application_status,
    application_reviews.decision
    FROM applications
    LEFT JOIN application_reviews
    ON applications.application_id = application_reviews.application_id
    ORDER BY applications.application_id"""
    rows = get_rows(query)
    show_rows(rows)


def add_application():
    print("\nRecord a new admission application")
    applicant_name = input("Applicant name: ")
    age = int(input("Age: "))
    gender = input("Gender (optional): ")
    guardian_name = input("Parent/guardian name: ")
    guardian_phone = input("Parent/guardian contact: ")
    relationship = input("Relationship to applicant: ")

    connection = connect_database()
    cursor = connection.cursor()

    guardian_query = "INSERT INTO guardians (name, phone, address) VALUES (%s, %s, %s)"
    cursor.execute(guardian_query, (guardian_name, guardian_phone, "Application record"))
    guardian_id = cursor.lastrowid

    application_query = """INSERT INTO applications
    (applicant_name, age, gender, guardian_id, relationship, application_status)
    VALUES (%s, %s, %s, %s, %s, %s)"""
    application_values = (
        applicant_name, age, gender, guardian_id, relationship, "Under Review"
    )
    cursor.execute(application_query, application_values)
    application_id = cursor.lastrowid

    review_query = """INSERT INTO application_reviews
    (application_id, care_need_checked, documents_checked,
    guardian_contacted, decision)
    VALUES (%s, %s, %s, %s, %s)"""
    review_values = (
        application_id, "Not checked", "Not checked",
        "Not checked", "Pending"
    )
    cursor.execute(review_query, review_values)

    connection.commit()
    cursor.close()
    connection.close()
    print("Application saved. A staff member must review it.")


def review_application():
    print("\nUpdate the human review checklist")
    application_id = int(input("Application ID: "))
    care_need = input("Care need checked? (Yes/No/Not checked): ")
    documents = input("Documents checked? (Yes/No/Not checked): ")
    guardian_contacted = input("Guardian contacted? (Yes/No/Not checked): ")
    decision = input("Decision by staff (Pending/Eligible/Not eligible): ")

    query = """UPDATE application_reviews
    SET care_need_checked = %s, documents_checked = %s,
    guardian_contacted = %s, decision = %s
    WHERE application_id = %s"""
    values = (care_need, documents, guardian_contacted, decision, application_id)

    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    if cursor.rowcount == 0:
        print("Application review was not found.")
    else:
        print("Review checklist updated. The decision was entered by staff.")
    cursor.close()
    connection.close()


def view_adoption_applications():
    query = """SELECT applicant_id, applicant_name, applicant_age, applicant_type,
    application_status, documents_status, home_study_status, eligibility_status
    FROM adoptive_applications ORDER BY applicant_id"""
    rows = get_rows(query)
    show_rows(rows)


def add_adoption_application():
    print("\nDemo intake form for prospective adoptive parents")
    applicant_name = input("Applicant name (or lead applicant name for a couple): ")
    applicant_age = int(input("Applicant age: "))
    applicant_type = input("Applicant type (Single/Couple): ")
    marital_status = input("Marital status: ")
    spouse_consent = input("Spouse consent (Yes/No/Not applicable): ")
    phone = input("Contact number or demo contact: ")
    address = input("Residential address or demo area: ")
    occupation = input("Occupation: ")
    family_children = int(input("Number of children currently in family: "))
    submitted_date = input("Date (YYYY-MM-DD): ")

    query = """INSERT INTO adoptive_applications
    (applicant_name, applicant_age, applicant_type, marital_status,
    spouse_consent, phone, address, occupation, family_children, submitted_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
        applicant_name, applicant_age, applicant_type, marital_status,
        spouse_consent, phone, address, occupation, family_children, submitted_date
    )
    save_record(query, values)
    print("This is a school-project intake record, not an official adoption application.")
    print("Applicants must use the official CARINGS process and authorised agencies.")


def review_adoption_application():
    print("\nRecord checklist results from an authorised review")
    applicant_id = int(input("Adoption applicant ID: "))
    documents_status = input("Required documents checked? (Pending/Checked): ")
    home_study_status = input("Home study report status (Pending/Complete): ")
    eligibility_status = input(
        "Official eligibility result (Pending/Verified Eligible/Not Eligible): "
    )
    application_status = input(
        "Application status (Submitted/In Review/Referred/Finalized/Closed): "
    )

    query = """UPDATE adoptive_applications
    SET documents_status = %s, home_study_status = %s,
    eligibility_status = %s, application_status = %s
    WHERE applicant_id = %s"""
    values = (
        documents_status, home_study_status, eligibility_status,
        application_status, applicant_id
    )

    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    if cursor.rowcount == 0:
        print("Adoption applicant record was not found.")
    else:
        print("Checklist saved. The program does not decide eligibility.")
    cursor.close()
    connection.close()


def record_official_child_clearance():
    child_id = int(input("Child ID: "))
    decision = input(
        "Has the CWC officially declared this child legally free for adoption? (Yes/No): "
    )
    if decision == "Yes":
        legal_status = "Legally Free for Adoption"
    else:
        legal_status = "Not Assessed or Not Declared"

    query = "UPDATE children SET adoption_legal_status = %s WHERE child_id = %s"
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(query, (legal_status, child_id))
    connection.commit()
    if cursor.rowcount == 0:
        print("Child record was not found.")
    else:
        print("The entered official clearance status was saved.")
    cursor.close()
    connection.close()


def record_completed_adoption():
    print("\nRecord a completed adoption after official approval")
    applicant_id = int(input("Adoptive applicant ID: "))
    child_id = int(input("Child ID: "))

    applicant_rows = get_rows(
        "SELECT eligibility_status FROM adoptive_applications WHERE applicant_id = %s",
        (applicant_id,)
    )
    child_rows = get_rows(
        "SELECT adoption_legal_status, care_status FROM children WHERE child_id = %s",
        (child_id,)
    )

    if len(applicant_rows) == 0:
        print("Adoptive applicant record was not found.")
        return
    if len(child_rows) == 0:
        print("Child record was not found.")
        return
    if applicant_rows[0][0] != "Verified Eligible":
        print("Record the official eligibility result before continuing.")
        return
    if child_rows[0][0] != "Legally Free for Adoption":
        print("Record official child clearance before continuing.")
        return
    if child_rows[0][1] != "In Care":
        print("This child is not marked as currently in care.")
        return

    order_date = input("Final adoption order date (YYYY-MM-DD): ")
    order_reference = input("Fictional or official order reference: ")

    connection = connect_database()
    cursor = connection.cursor()
    query = """INSERT INTO adoption_cases
    (child_id, applicant_id, order_date, order_reference)
    VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (child_id, applicant_id, order_date, order_reference))
    cursor.execute(
        "UPDATE children SET care_status = 'Adopted' WHERE child_id = %s",
        (child_id,)
    )
    cursor.execute(
        "UPDATE adoptive_applications SET application_status = 'Finalized' "
        "WHERE applicant_id = %s",
        (applicant_id,)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("Completed adoption record saved from the entered official order.")


def view_completed_adoptions():
    query = """SELECT adoption_cases.adoption_id, children.child_id,
    adoptive_applications.applicant_id, adoption_cases.order_date,
    adoption_cases.order_reference
    FROM adoption_cases
    JOIN children ON adoption_cases.child_id = children.child_id
    JOIN adoptive_applications
    ON adoption_cases.applicant_id = adoptive_applications.applicant_id
    ORDER BY adoption_cases.order_date"""
    rows = get_rows(query)
    show_rows(rows)


def view_support_summary():
    print("This table contains fictional totals only, with no child names or IDs.")
    query = """SELECT support_category, SUM(child_count)
    FROM support_summary GROUP BY support_category ORDER BY support_category"""
    rows = get_rows(query)
    show_rows(rows)


def view_staff():
    query = "SELECT staff_id, name, job_title, phone, work_status FROM staff ORDER BY staff_id"
    rows = get_rows(query)
    show_rows(rows)


def add_staff():
    print("\nAdd a staff record")
    name = input("Staff name: ")
    job_title = input("Job title: ")
    phone = input("Contact number or demo contact: ")

    query = """INSERT INTO staff (name, job_title, phone, work_status)
    VALUES (%s, %s, %s, %s)"""
    values = (name, job_title, phone, "Active")
    save_record(query, values)


def update_staff_status():
    staff_id = int(input("Staff ID: "))
    work_status = input("New status (Active/On Leave/Inactive): ")
    query = "UPDATE staff SET work_status = %s WHERE staff_id = %s"

    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(query, (work_status, staff_id))
    connection.commit()
    if cursor.rowcount == 0:
        print("Staff record was not found.")
    else:
        print("Staff status updated.")
    cursor.close()
    connection.close()


def add_donation():
    print("\nRecord a donation")
    donor_name = input("Donor name or Anonymous: ")
    donation_date = input("Date (YYYY-MM-DD): ")
    amount = float(input("Amount in rupees: "))
    purpose = input("Purpose (general, books, food, etc.): ")

    query = """INSERT INTO donations (donor_name, donation_date, amount, purpose)
    VALUES (%s, %s, %s, %s)"""
    values = (donor_name, donation_date, amount, purpose)
    save_record(query, values)


def add_expense():
    print("\nRecord an expense")
    expense_date = input("Date (YYYY-MM-DD): ")
    category = input("Category (food, education, health, etc.): ")
    amount = float(input("Amount in rupees: "))
    details = input("Short description: ")

    query = """INSERT INTO expenses (expense_date, category, amount, details)
    VALUES (%s, %s, %s, %s)"""
    values = (expense_date, category, amount, details)
    save_record(query, values)


def view_inventory():
    query = """SELECT item_id, item_name, quantity, reorder_level
    FROM inventory ORDER BY item_name"""
    rows = get_rows(query)
    show_rows(rows)


def update_inventory():
    item_id = int(input("Inventory item ID: "))
    quantity = int(input("New quantity: "))
    query = "UPDATE inventory SET quantity = %s WHERE item_id = %s"

    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(query, (quantity, item_id))
    connection.commit()
    if cursor.rowcount == 0:
        print("Inventory item was not found.")
    else:
        print("Inventory quantity updated.")
    cursor.close()
    connection.close()


def make_charts():
    print("\nCreating charts from the MySQL records.")
    print("Each chart helps with a different planning question.")

    class_rows = get_rows(
        "SELECT school_class, COUNT(*) FROM children "
        "WHERE care_status = 'In Care' GROUP BY school_class ORDER BY school_class"
    )
    class_data = pd.DataFrame(class_rows, columns=["Class", "Children"])

    application_rows = get_rows(
        "SELECT application_status, COUNT(*) FROM applications "
        "GROUP BY application_status ORDER BY application_status"
    )
    application_data = pd.DataFrame(
        application_rows, columns=["Status", "Applications"]
    )

    donation_rows = get_rows(
        "SELECT MONTH(donation_date), SUM(amount) FROM donations "
        "GROUP BY MONTH(donation_date) ORDER BY MONTH(donation_date)"
    )
    donation_data = pd.DataFrame(
        donation_rows, columns=["MonthNumber", "TotalAmount"]
    )

    expense_rows = get_rows(
        "SELECT category, SUM(amount) FROM expenses "
        "GROUP BY category ORDER BY category"
    )
    expense_data = pd.DataFrame(
        expense_rows, columns=["Category", "TotalAmount"]
    )

    plt.figure()
    plt.bar(class_data["Class"], class_data["Children"], color="skyblue")
    plt.title("Children by School Class")
    plt.xlabel("School class")
    plt.ylabel("Number of children")

    plt.figure()
    plt.bar(application_data["Status"], application_data["Applications"],
            color="orange")
    plt.title("Admission Applications by Status")
    plt.xlabel("Application status")
    plt.ylabel("Number of applications")
    plt.xticks(rotation=20)

    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    donation_months = []
    for month_number in donation_data["MonthNumber"]:
        donation_months.append(month_names[month_number - 1])

    plt.figure()
    plt.plot(donation_months, donation_data["TotalAmount"],
             marker="o", color="green")
    plt.title("Donations by Month")
    plt.xlabel("Month")
    plt.ylabel("Donation amount in rupees")
    plt.xticks(rotation=30)

    plt.figure()
    plt.bar(expense_data["Category"], expense_data["TotalAmount"],
            color="salmon")
    plt.title("Expenses by Category")
    plt.xlabel("Expense category")
    plt.ylabel("Amount in rupees")
    plt.xticks(rotation=20)

    adoption_rows = get_rows(
        "SELECT YEAR(order_date), COUNT(*) FROM adoption_cases "
        "GROUP BY YEAR(order_date) ORDER BY YEAR(order_date)"
    )
    adoption_data = pd.DataFrame(
        adoption_rows, columns=["Year", "CompletedAdoptions"]
    )

    support_rows = get_rows(
        "SELECT support_category, SUM(child_count) FROM support_summary "
        "GROUP BY support_category ORDER BY support_category"
    )
    support_data = pd.DataFrame(
        support_rows, columns=["SupportCategory", "Children"]
    )

    plt.figure()
    plt.bar(adoption_data["Year"], adoption_data["CompletedAdoptions"],
            color="purple")
    plt.title("Completed Adoptions by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of completed adoptions")

    plt.figure()
    plt.bar(support_data["SupportCategory"], support_data["Children"],
            color="teal")
    plt.title("Separate Child-Support Services: Anonymous Demo Counts")
    plt.xlabel("Fictional support group")
    plt.ylabel("Number of cases")
    plt.xticks(rotation=20)

    plt.show()


def show_menu():
    print("\nORPHANAGE HOME MANAGEMENT SYSTEM")
    print("1. View children")
    print("2. Add a child")
    print("3. View parents and guardians")
    print("4. Add a parent or guardian")
    print("5. Link a guardian to a child")
    print("6. View linked child and guardian records")
    print("7. View admission applications")
    print("8. Add an admission application")
    print("9. Update an application review")
    print("10. View staff")
    print("11. Add a staff member")
    print("12. Update staff work status")
    print("13. Record a donation")
    print("14. Record an expense")
    print("15. View inventory")
    print("16. Update inventory quantity")
    print("17. View adoption applications")
    print("18. Add a prospective adoptive parent application")
    print("19. Review adoption documents and official eligibility result")
    print("20. Record official child adoption clearance")
    print("21. Record completed adoption from an official order")
    print("22. View completed adoptions")
    print("23. View anonymous support summary")
    print("24. Show data charts")
    print("0. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_children()
    elif choice == "2":
        add_child()
    elif choice == "3":
        view_guardians()
    elif choice == "4":
        add_guardian()
    elif choice == "5":
        link_guardian()
    elif choice == "6":
        view_child_guardians()
    elif choice == "7":
        view_applications()
    elif choice == "8":
        add_application()
    elif choice == "9":
        review_application()
    elif choice == "10":
        view_staff()
    elif choice == "11":
        add_staff()
    elif choice == "12":
        update_staff_status()
    elif choice == "13":
        add_donation()
    elif choice == "14":
        add_expense()
    elif choice == "15":
        view_inventory()
    elif choice == "16":
        update_inventory()
    elif choice == "17":
        view_adoption_applications()
    elif choice == "18":
        add_adoption_application()
    elif choice == "19":
        review_adoption_application()
    elif choice == "20":
        record_official_child_clearance()
    elif choice == "21":
        record_completed_adoption()
    elif choice == "22":
        view_completed_adoptions()
    elif choice == "23":
        view_support_summary()
    elif choice == "24":
        make_charts()
    elif choice == "0":
        print("Thank you.")
        break
    else:
        print("Please enter a number from the menu.")
