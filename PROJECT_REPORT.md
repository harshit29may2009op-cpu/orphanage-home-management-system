# Project Report: Orphanage Home Management System

## 1. Introduction

A children's home maintains information about children, parents or guardians, staff, admission requests, donations, expenses, and supplies. Paper registers can make it difficult to find a record or prepare a quick summary. This project demonstrates a simple computer-based way to organise fictional records and display useful summaries.

The project is designed for a Class 12 CBSE Informatics Practices student. It uses basic Python, MySQL, Pandas, and Matplotlib. The sample database has exactly 35 fictional child records, including 3 fictional finalized adoption cases.

## 2. Objectives

- Store child records in a MySQL database.
- Keep guardian and staff details in separate tables.
- Link guardians to children using database keys.
- Record admission applications and a checklist for human review.
- Collect a basic prospective-adopter intake and record official review statuses.
- Record completed adoption cases only after entering official clearance and order details.
- Record donations, expenses, and basic supply quantities.
- Use charts to help with education, admission workload, donation, budget, adoption, and service planning.
- Keep juvenile-justice support counts separate and anonymous in the public demonstration.
- Demonstrate Python, SQL, Pandas, and Matplotlib in a practical context.

## 3. Problem and proposed solution

**Problem:** Staff may need to search several paper records to learn how many children are in a class, which applications are waiting for review, how donations change over time, or which expense categories use more funds.

**Solution:** This menu-based Python program saves sample records in MySQL. A staff member can select an operation from the menu. Pandas organizes grouped database results into DataFrames, and Matplotlib displays the summaries as charts.

The program stores and presents information. A responsible person reviews admission applications and enters decisions. Adoption has a separate prospective-adopter intake and review. The software does not determine eligibility, match applicants and children, or replace a legal adoption process.

## 4. Tools and concepts

- **Python:** functions, variables, input and output, while loop, if/elif/else, and basic database commands.
- **MySQL:** database tables, primary keys, foreign keys, SELECT, INSERT, UPDATE, JOIN, COUNT, and SUM.
- **Pandas:** DataFrames made from MySQL query results.
- **Matplotlib:** bar charts and a line chart with titles and axis labels.
- **MySQL Connector/Python:** connection between Python and the MySQL database.

## 5. Main features

1. View and add child records.
2. View and add parent/guardian records.
3. Link a guardian to a child and display linked details.
4. View admission applications and enter checklist results.
5. Add staff and update a staff member's work status.
6. Record donations and expenses.
7. View inventory and update a supply quantity.
8. Enter basic prospective-adopter details: applicant age, single/couple type, marital status, spouse consent where applicable, contact, address, occupation, and number of children in the household.
9. Track document-check and home-study status, with the eligibility result entered only from an authorised review.
10. Enter a child's legal-clearance status only after the relevant official decision is recorded.
11. Record a completed adoption only when the database shows the applicant as officially verified and the child as officially cleared, and a final-order date and reference are entered.
12. Display six data visualisations.

The adoption intake is only a school exercise. CARA directs prospective adoptive parents to register through the official CARINGS portal. It refers applicants to Section 57 of the Juvenile Justice Act and Regulation 5 of the Adoption Regulations, 2022 for eligibility, and Schedule VI for online registration details and documents. The official criteria cover applicant fitness and circumstances; requirements such as family consent, age criteria, documentation, and home study may apply. The precise rules depend on the case and can change. This project does not calculate legal eligibility. It records review statuses entered by an authorised person and does not store copies of identity, income, medical, criminal-history, or family documents. The official process and criteria must be checked with CARA and the authorised agency. See the [Ministry of Women and Child Development's CARA guidance](https://www.wcd.gov.in/prospective-adoptive-parents/cara), the [Adoption Regulations, 2022](https://cara.wcd.gov.in/PDF/adoption_regulations_2022_2709.pdf), and [Schedule VI](https://cara.wcd.gov.in/pdf/schedule/6.pdf).

## 6. Database design

The project uses separate related tables. The ID in each table identifies a record. Foreign keys connect related records.

| Table | Information stored |
|---|---|
| children | Child ID, name, age, optional gender, school class, care status, official adoption-clearance status |
| guardians | Guardian ID, name, contact, address |
| child_guardians | Child ID, guardian ID, relationship |
| applications | Admission application details and guardian ID |
| application_reviews | Admission checklist items and staff-entered decision |
| adoptive_applications | Basic applicant details, household details, and review status |
| adoption_cases | Child ID, applicant ID, final-order date, and order reference |
| staff | Staff ID, name, job title, contact, work status |
| donations | Donor name, date, amount, purpose |
| expenses | Date, category, amount, details |
| inventory | Item name, quantity, reorder level |
| support_summary | Anonymous aggregate counts with no child ID or name |

A child may have more than one guardian, so child_guardians is a separate linking table. Juvenile-justice support totals are kept in support_summary and are not linked to children records. The two example juvenile-justice cases are a separate fictional service count; they are not described as children living in the home.

## 7. Charts and their use

All chart data comes from grouped MySQL queries and is placed into Pandas DataFrames before Matplotlib plots it.

### Chart 1: Children by school class

A bar chart counts children currently in care by class. It can help staff plan books, classroom support, or tutoring time.

### Chart 2: Admission applications by status

A bar chart counts admission applications in each status. It can show the review workload.

### Chart 3: Donations by month

A line chart adds donation amounts by month. It shows how donations change during the year and can support basic planning.

### Chart 4: Expenses by category

A bar chart adds recorded expenses by category. It can help staff understand where the budget is being spent.

### Chart 5: Completed adoptions by year

A bar chart counts adoption cases by the year of the final order. It uses only completed sample records that contain an order date and reference; it does not predict or recommend a match.

### Chart 6: Separate child-support services

A bar chart shows fictional aggregate counts for children currently in care and separate juvenile-justice support cases. It has no names or child IDs. Children in the home are not labelled as being in conflict with the law.

## 8. How to use the program

1. Run database/schema.sql to create the database and tables.
2. Run database/sample_data.sql once to insert fictional demonstration records.
3. Enter local MySQL connection details in config.py.
4. Install the Python libraries in requirements.txt.
5. Run main.py and choose a task from the menu.
6. Use options 17 to 23 for adoption records and the anonymous support summary.
7. Select option 24 to display the charts.

## 9. Testing by a student

- View the 35 child records and check that 32 are in care and 3 have sample adopted status.
- Add a child and view the list again.
- Add a guardian, link that record to a child, and view linked records.
- Add a staff member and change the work status.
- Add sample donations and expenses, then display their charts.
- Add an admission application and update its human-review checklist.
- Add a prospective-adopter application and enter a pending review result.
- Confirm that a completed adoption is blocked unless the applicant and child have the required recorded official statuses.
- View the yearly adoption chart and confirm it counts only rows in adoption_cases.
- View the separate anonymous support summary and confirm that it contains no child name or ID.

## 10. Limitations and future improvement

This is a basic school project, not a system ready for a real children's home or adoption agency. The demonstration records are fictional. The program has no user login, role-based access, automatic backups, or graphical interface. It cannot validate official documents or check eligibility against current laws. The adoption process changes and depends on individual circumstances, so no rule is hard-coded. Real records about children and families must not be added to a public repository.

Possible future improvements include input validation, a login system, safe backups, search by name or ID, and a graphical interface. These features are outside the simple Class 12 demonstration.

## 11. Conclusion

The project shows how Python and MySQL can organise related records for a practical problem. Pandas and Matplotlib turn selected database summaries into charts. The adoption workflow records only staff or authority review outcomes, while important decisions remain with authorised people. The separate support chart demonstrates privacy-conscious aggregate reporting.

## 12. Viva preparation

**Why did you use MySQL?**  
It stores related information in organised tables and allows records to be searched and updated.

**Why are guardians stored separately?**  
A child can have more than one guardian, and guardian details can be linked to a child through a separate table.

**How does the adoption module check eligibility?**  
It does not calculate eligibility. It stores an outcome entered after authorised review. It also requires official child-clearance status and an entered final-order reference before recording a completed case.

**Why is juvenile-justice information not linked to child names?**  
It is sensitive. The demonstration needs only an anonymous total for planning, so it does not label or expose any individual child.

**How are the charts made?**  
MySQL groups the records, Pandas puts the results into DataFrames, and Matplotlib draws bar or line charts.

## 13. References

- CBSE, Informatics Practices, Class XII, Curriculum 2026–27: https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/Informatics_Practices_SecP2_2026-27.pdf
- Ministry of Women and Child Development, CARA guidance: https://www.wcd.gov.in/prospective-adoptive-parents/cara
- Adoption Regulations, 2022: https://cara.wcd.gov.in/PDF/adoption_regulations_2022_2709.pdf
- Schedule VI, online registration and document list: https://cara.wcd.gov.in/pdf/schedule/6.pdf
- Official CARINGS portal: https://carings.wcd.gov.in/
- Python documentation: https://docs.python.org/3/
- MySQL documentation: https://dev.mysql.com/doc/
- Pandas documentation: https://pandas.pydata.org/docs/
- Matplotlib documentation: https://matplotlib.org/stable/
