# Orphanage Home Management System

A Class 12 Python + MySQL project for managing a fictional home's admissions workflow, child profiles, family contacts, education records, donations, expenses, and inventory. Matplotlib generates four aggregate charts from the database.

> This is a school demonstration, not software for making real placement decisions or storing real children's information. The sample data is fictional. Gender is never used to determine eligibility. Checklist progress and decisions are entered by a human reviewer; the program does not decide who qualifies.

## Features

- MySQL database with linked tables for children, parents/guardians, admission applications, review checklists, staff, education, donors, donations, expenses, and inventory.
- Human-reviewed admission workflow with configurable checklist items. The sample checklist is for demonstrating record keeping, not legal guidance or a statement of eligibility rules.
- Record and search child profiles; register and review applications; record donors, donations, expenses, school progress, and stock movements.
- Dashboard with record counts and low-stock alerts.
- Four Matplotlib charts: children by recorded gender, application workflow status, donations by month, and expenses by category. Charts use aggregates and do not show names.
- Repeatable synthetic dataset with about 2,835 rows so charts and database queries have useful sample volume.

## Requirements

- Python 3.10 or later
- MySQL Server
- Packages listed in requirements.txt

## Setup

1. Create the database in MySQL Workbench by opening and running database/schema.sql, or use a terminal:

   ~~~sh
   mysql -u root -p < database/schema.sql
   ~~~

2. Install the Python packages:

   ~~~sh
   python -m pip install -r requirements.txt
   ~~~

3. Copy .env.example to .env and enter your local MySQL connection values. Keep .env private; it is ignored by Git.

   ~~~sh
   cp .env.example .env
   ~~~

   On Windows, copy the file in File Explorer or use copy .env.example .env in Command Prompt.

4. Load fictional sample records:

   ~~~sh
   python database/seed_demo.py
   ~~~

   The seed script stops if child records already exist, to avoid accidental duplicate demo data. Use a fresh orphanage_demo database for a clean sample load.

5. Start the menu:

   ~~~sh
   python main.py
   ~~~

6. Choose option 12 to create charts in charts_output/.

## Database overview

- children and caregivers are connected through child_caregivers.
- admission_applications stores referral and parent/guardian context.
- review_criteria and application_reviews track review progress without calculating eligibility.
- education_records, donors, donations, expenses, inventory_items, and inventory_movements support the reporting and resource-management features.

All queries entered by the program use placeholders for user-supplied values. Keep real passwords out of code and GitHub. Use only fictional data in this public project. For a real service, privacy, access control, retention, safeguarding, and local legal review would need to be designed by qualified people.

## Project report

See PROJECT_REPORT.md for the aim, objectives, workflow, database design, chart descriptions, limitations, and viva questions.
