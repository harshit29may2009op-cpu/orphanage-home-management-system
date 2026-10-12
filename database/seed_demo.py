"""Generate a small, repeatable, entirely fictional class-project dataset."""
from datetime import date, timedelta
from decimal import Decimal
import random
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from config import connect_db  # noqa: E402

RNG = random.Random(12012)
GENDERS = ["Girl", "Boy", "Another identity", "Prefer not to say"]
START_DATE = date(2024, 1, 1)


def demo_date(max_days=850):
    return START_DATE + timedelta(days=RNG.randint(0, max_days))


def main():
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM children")
        if cursor.fetchone()[0]:
            print("Demo seed skipped: child rows already exist. Use a fresh v2 demo database.")
            return

        roles = ["Coordinator", "Educator", "Care worker", "Nurse",
                 "Cook", "Administrator", "Tutor", "Volunteer coordinator"]
        staff = [
            (i, f"DEMO-STAFF-{i:02}", f"DEMO Staff {i:02}", role, True)
            for i, role in enumerate(roles, start=1)
        ]
        cursor.executemany(
            "INSERT INTO staff_members "
            "(staff_id, staff_code, display_name, role_name, is_active) "
            "VALUES (%s, %s, %s, %s, %s)",
            staff,
        )

        children = []
        for i in range(1, 36):
            born = date(2008, 1, 1) + timedelta(days=RNG.randint(0, 5000))
            children.append((
                i, f"DEMO-CH-{i:03}", f"DEMO CHILD {i:03}", born,
                RNG.choice(GENDERS), demo_date(700), f"Grade {RNG.randint(1, 12)}",
                f"DEMO School {RNG.randint(1, 5):02}", "In care",
            ))
        cursor.executemany(
            "INSERT INTO children "
            "(child_id, child_code, display_name, date_of_birth, gender, "
            "admission_date, school_grade, school_name, care_status) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            children,
        )

        parents = [
            (i, f"DEMO Parent or Guardian {i:02}", "DEMO ONLY")
            for i in range(1, 19)
        ]
        cursor.executemany(
            "INSERT INTO parents_guardians "
            "(parent_guardian_id, display_name, contact_reference) "
            "VALUES (%s, %s, %s)",
            parents,
        )
        child_links = [
            (i, ((i - 1) // 2) + 1,
             RNG.choice(["Parent", "Guardian", "Relative"]),
             RNG.choice(["Not reviewed", "Pending review",
                         "Reviewed by authorized person"]))
            for i in range(1, 36)
        ]
        cursor.executemany(
            "INSERT INTO child_parent_links "
            "(child_id, parent_guardian_id, relationship_to_child, authority_review_status) "
            "VALUES (%s, %s, %s, %s)",
            child_links,
        )

        sources = ["Community referral", "School referral",
                   "Social worker referral", "Demo outreach"]
        applications = []
        for i in range(1, 26):
            status = RNG.choice(
                ["Pending review", "Approved by reviewer", "Referred", "Closed"]
            )
            reviewer = None if status == "Pending review" else f"DEMO Reviewer {RNG.randint(1, 8):02}"
            note = None if status == "Pending review" else "DEMO human-entered workflow status"
            decision_date = None if status == "Pending review" else demo_date()
            applications.append((
                i, f"DEMO-APP-{i:03}", f"DEMO APPLICANT {i:03}",
                RNG.randint(2, 17), RNG.choice(GENDERS), demo_date(),
                RNG.choice(sources), status, reviewer, note, decision_date,
            ))
        cursor.executemany(
            "INSERT INTO admission_applications "
            "(application_id, application_code, applicant_display_name, age_years, "
            "gender, received_on, referral_source, status, reviewer_name, "
            "reviewer_note, decision_on) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            applications,
        )

        application_parents = [
            (i, ((i - 1) % 18) + 1,
             RNG.choice(["Parent", "Relative", "Guardian"]))
            for i in range(1, 26)
        ]
        cursor.executemany(
            "INSERT INTO application_parent_links "
            "(application_id, parent_guardian_id, relationship_to_applicant) "
            "VALUES (%s, %s, %s)",
            application_parents,
        )

        cursor.execute("SELECT criterion_id FROM review_criteria WHERE is_active = TRUE")
        criteria = [row[0] for row in cursor.fetchall()]
        reviews = []
        for app_id in range(1, 26):
            for criterion_id in criteria:
                status = RNG.choice(["Not started", "In review", "Reviewed"])
                reviewer = None if status == "Not started" else f"DEMO Reviewer {RNG.randint(1, 8):02}"
                reviewed_on = None if status == "Not started" else demo_date()
                reviews.append((app_id, criterion_id, status, reviewer, reviewed_on))
        cursor.executemany(
            "INSERT INTO application_reviews "
            "(application_id, criterion_id, review_status, reviewer_name, reviewed_on) "
            "VALUES (%s, %s, %s, %s, %s)",
            reviews,
        )

        education = [
            (i, RNG.choice(["2024-25", "2025-26", "2026-27"]),
             f"Grade {RNG.randint(1, 12)}",
             Decimal(str(round(RNG.uniform(65, 100), 2))),
             Decimal(str(round(RNG.uniform(55, 98), 2))))
            for i in range(1, 36)
        ]
        cursor.executemany(
            "INSERT INTO education_records "
            "(child_id, academic_year, school_grade, attendance_percent, result_percent) "
            "VALUES (%s, %s, %s, %s, %s)",
            education,
        )

        donors = [
            (i, f"DEMO-DONOR-{i:02}", f"DEMO Donor {i:02}", "DEMO ONLY")
            for i in range(1, 13)
        ]
        cursor.executemany(
            "INSERT INTO donors (donor_id, donor_code, display_name, contact_reference) "
            "VALUES (%s, %s, %s, %s)",
            donors,
        )
        donations = [
            (RNG.randint(1, 12), demo_date(), Decimal(RNG.randint(500, 20000)),
             RNG.choice(["Education", "Food", "Health", "General"]),
             RNG.choice(["Demo transfer", "Demo UPI", "Demo cash"]))
            for _ in range(60)
        ]
        cursor.executemany(
            "INSERT INTO donations (donor_id, donated_on, amount, purpose, payment_method) "
            "VALUES (%s, %s, %s, %s, %s)",
            donations,
        )

        expenses = [
            (demo_date(), RNG.choice(["Food", "Education", "Health", "Clothing", "Utilities"]),
             Decimal(RNG.randint(250, 12000)), "DEMO ONLY synthetic expense")
            for _ in range(45)
        ]
        cursor.executemany(
            "INSERT INTO expenses (spent_on, category, amount, description) "
            "VALUES (%s, %s, %s, %s)",
            expenses,
        )

        item_rows = []
        movement_rows = []
        for item_id in range(1, 11):
            on_hand = 0
            for _ in range(4):
                movement_type = "IN" if on_hand < 10 or RNG.random() < 0.62 else "OUT"
                quantity = RNG.randint(1, 12)
                if movement_type == "OUT":
                    quantity = min(quantity, on_hand)
                    if quantity == 0:
                        movement_type = "IN"
                        quantity = RNG.randint(1, 12)
                on_hand += quantity if movement_type == "IN" else -quantity
                movement_rows.append((
                    item_id, movement_type, quantity, demo_date(),
                    "DEMO ONLY stock movement",
                ))
            item_rows.append((
                item_id, f"DEMO-ITEM-{item_id:02}",
                f"DEMO Supply {item_id:02}",
                RNG.choice(["Food", "Education", "Health", "Clothing"]),
                RNG.choice(["units", "packs", "kg"]), on_hand, 8,
            ))
        cursor.executemany(
            "INSERT INTO inventory_items "
            "(item_id, item_code, item_name, category, unit_name, quantity_on_hand, reorder_level) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            item_rows,
        )
        cursor.executemany(
            "INSERT INTO inventory_movements "
            "(item_id, movement_type, quantity, moved_on, purpose) "
            "VALUES (%s, %s, %s, %s, %s)",
            movement_rows,
        )

        connection.commit()
        print("Fictional demo data loaded successfully.")
        print("35 children, 8 staff members, and about 478 total rows.")
        print("Names and contact references are DEMO placeholders.")
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Could not seed the demo database: {error}")
        print("Check MySQL is running, the revised schema was imported, and .env is set.")
