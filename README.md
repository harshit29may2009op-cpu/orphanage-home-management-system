# Orphanage Home Management System

A small Python and MySQL project for a Class 12 CBSE Informatics Practices student. It models everyday record-keeping at a children's home and shows how data charts can support planning.

## The real-life problem

A children's home may need to find child, guardian, staff, admission, donation, expense, and supply information quickly. Paper registers can make it harder to find a record or prepare a useful summary. This menu-based program stores fictional example records in MySQL and uses Pandas and Matplotlib to present summaries.

The sample database contains exactly **35 fictional child records**: 32 children currently in care and 3 sample completed adoptions. Parents/guardians and staff are stored in separate tables. The adopter details, phone numbers, names, and order references are also fictional.

## What it can do

- View and add child records.
- Maintain parent/guardian records separately and link them to children.
- Record admission applications and staff-reviewed checklist results.
- Add staff, update staff status, record donations and expenses, and update inventory.
- Record a separate prospective-adopter intake with basic fields such as applicant age, family status, spouse consent where applicable, contact, address, occupation, and household children.
- Track a document checklist, home-study status, and an eligibility result entered from an authorised review.
- Record a completed adoption only after the database has both a recorded official eligibility result and a child-clearance status, then store the final-order date and reference.
- Keep juvenile-justice support cases in a **separate aggregate-only table**. This fictional count has no child names or IDs and is not linked to the 35 child records.

The adoption form is a classroom demonstration, not a legal application. It records the applicant type, family status, consent where applicable, basic contact details, document-check status, home-study status, and an eligibility result entered by an authorised reviewer. Age/family criteria and the child's legal clearance must be checked under current official rules. It does not decide who is eligible, match a child with an applicant, or replace CARA, CARINGS, a Child Welfare Committee, or an authorised agency. The Government of India Ministry of Women and Child Development directs prospective adoptive parents to register through the official CARINGS portal and refers them to the applicable adoption rules and document schedules. See [CARA official guidance](https://www.wcd.gov.in/prospective-adoptive-parents/cara) and the [Adoption Regulations, 2022](https://cara.wcd.gov.in/PDF/adoption_regulations_2022_2709.pdf). The program stores checklist status only; it does not store copies of sensitive documents.

## Matplotlib charts

Menu option 24 creates six charts from MySQL query results:

1. **Children by school class:** helps plan books and teaching support for children currently in care.
2. **Admission applications by status:** helps staff see the review workload.
3. **Donations by month:** shows how donations change during the year.
4. **Expenses by category:** helps with simple budget planning.
5. **Completed adoptions by year:** counts only finalized demo cases with an entered order reference.
6. **Separate child-support services:** displays anonymous fictional totals, including a separate juvenile-justice support count. It does not identify or classify any child record.

## Simple technology used

- Python: functions, variables, input/output, loops, conditions, and SQL commands.
- MySQL: tables, primary keys, foreign keys, joins, and grouped queries.
- Pandas: puts query results into DataFrames for charting.
- Matplotlib: creates bar and line charts.

These topics match Class XII Informatics Practices topics such as Pandas, data visualisation, and SQL. See the [CBSE Class XII Informatics Practices syllabus](https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Informatics_Practices_SecP2_2026-27.pdf).

## Run the project

1. Install Python and MySQL on your computer.
2. Open database/schema.sql in MySQL Workbench and run it.
3. Open database/sample_data.sql in MySQL Workbench and run it once.
4. Open config.py and enter your local MySQL password. Keep your real password private.
5. Install the libraries listed in requirements.txt with pip install -r requirements.txt.
6. Start the program with python main.py.
7. Choose menu option 24 to open the charts. Close the chart windows to return to the menu.

## Database tables

| Table | Purpose |
|---|---|
| children | Child, school, care status, and officially recorded adoption-clearance status |
| guardians | Separate parent/guardian contact records |
| child_guardians | Links children with guardians and records their relationship |
| applications | Admission application and guardian link |
| application_reviews | Staff-entered checklist and decision |
| adoptive_applications | Basic prospective-adopter intake and review statuses |
| adoption_cases | Completed adoption date and official-order reference |
| staff | Staff role and work status |
| donations | Donor, date, amount, and purpose |
| expenses | Date, category, amount, and details |
| inventory | Supply quantity and reorder level |
| support_summary | Fictional service totals with no child identifiers |

## Project scope and privacy

This is a school demonstration, not a real case-management system. All records are synthetic. Never put real children's, families', adoptive applicants', or juvenile-justice information in a public GitHub repository. A real service would need lawful access, trained staff, privacy safeguards, secure permissions, and backups. A child's conflict-with-law support needs are sensitive; this sample intentionally stores only a fictional aggregate count in a separate table.

Project report: see PROJECT_REPORT.md.
