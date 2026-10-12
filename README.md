# Orphanage Home Management System

A Class 12 Python + MySQL project for managing a fictional home's admissions workflow, child profiles, separately stored parent/guardian records, staff, education, donations, expenses, and inventory. Matplotlib creates four aggregate charts from the database.

> This is a school demonstration, not software for real placement decisions or real children's information. The sample database contains exactly 35 fictional child records. Gender is not used to determine eligibility. Checklist progress and decisions are entered by a human reviewer.

## Features

- MySQL tables link children, parents/guardians, admission applications, review checklists, staff, education, donors, donations, expenses, and inventory.
- Separate parent/guardian records can be added, listed, and linked to children. Application contacts are stored separately from application records.
- Staff management supports adding, listing, and updating staff role/active status.
- Admissions workflow tracks configurable review items without scoring eligibility or giving legal guidance.
- Record/search child profiles; record education, donations, expenses, and stock movements.
- Dashboard shows record counts and low-stock alerts.
- Four Matplotlib charts: children by recorded gender, application workflow status, donations by month, and expenses by category.
- Small fictional dataset: 35 children and about 478 total rows across all tables.

## Requirements

- Python 3.10 or later
- MySQL Server
- Packages listed in requirements.txt

## Setup

1. Create the revised demo database by running database/schema.sql in MySQL Workbench, or use:

   ~~~sh
   mysql -u root -p < database/schema.sql
   ~~~

   The revised schema uses a new database name, orphanage_class12_demo_v2, so it does not overwrite the earlier demo database.

2. Install packages:

   ~~~sh
   python -m pip install -r requirements.txt
   ~~~

3. Copy .env.example to .env and set your local MySQL connection values. Keep .env private; Git ignores it.

   ~~~sh
   cp .env.example .env
   ~~~

4. Load the fictional sample records:

   ~~~sh
   python database/seed_demo.py
   ~~~

   The seed script stops if the new database already contains child rows.

5. Start the menu:

   ~~~sh
   python main.py
   ~~~

6. Choose option 12 to create charts in charts_output/. Options 13 and 14 open staff and parent/guardian management.

All SQL values entered by the program use query placeholders. Use fictional data only. A real service would need qualified privacy, access-control, safeguarding, retention, and local legal review.

## Project report

See PROJECT_REPORT.md for objectives, workflow, database design, chart descriptions, limitations, and viva questions.
