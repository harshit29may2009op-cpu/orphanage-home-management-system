# Class 12 Computer Science Project Report

## Project title

Orphanage Home Management System — a Python and MySQL demonstration project

**Student:** ____________________  
**Class/section:** ____________________  
**School:** ____________________  
**Teacher:** ____________________

## Abstract

This project demonstrates how Python and MySQL can organize records for a fictional care home. It includes 35 fictional child profiles, separately stored parent/guardian records, staff management, an admission-review checklist, education records, donations, expenses, and inventory. Matplotlib creates four aggregate charts to summarize the sample data.

The program records workflow information. It does not decide whether a child is eligible for placement. A qualified human must review each application and follow the applicable local process.

## Problem statement and objectives

Paper-based records can be difficult to search and summarize. This project uses linked MySQL tables and a Python menu to make sample records easier to manage.

1. Store related records using primary and foreign keys.
2. Keep parent/guardian records separate from child and application records.
3. Add, list, and update staff roles/status.
4. Track admission checklist progress and a human-entered status.
5. Record education, donation, expense, and inventory activity.
6. Generate at least three charts with Matplotlib.

## Main modules

- **Child records:** add, search, and list demo profiles.
- **Parent/guardian records:** create a separate record, link it to a child, and track review status.
- **Staff management:** add staff, list staff, and update role or active status.
- **Admissions:** record a referral and link a separately stored parent/guardian.
- **Review checklist:** track items as not started, in review, or reviewed. It is not an eligibility score.
- **Education, finance, and inventory:** record school progress, donations, expenses, and stock movements.
- **Charts:** create four PNG charts from aggregate MySQL queries.

## Database design

The schema separates children, parents_guardians, child_parent_links, admission_applications, application_parent_links, review criteria, review progress, staff, education, donors, donations, expenses, inventory items, and inventory movements. Primary keys identify rows; foreign keys connect related records.

## Charts

1. **Children by recorded gender:** counts the synthetic dataset by category. Gender is not used in admission decisions.
2. **Application workflow:** counts applications by their human-entered status.
3. **Donations by month:** monthly totals from fictional records.
4. **Expenses by category:** totals grouped by expense category.

## Privacy and fairness choices

- The public sample uses DEMO labels and has exactly 35 fictional child records.
- Parent/guardian information is stored separately and linked through relationship tables.
- Charts show aggregate counts and totals, not names.
- Gender does not determine eligibility.
- The checklist records review progress only. The program does not encode local legal rules or make placement decisions.
- This learning project has no authentication, role-based access, encryption, or production safeguards. Do not enter real personal or safeguarding information.

## Conclusion and future scope

The project demonstrates relational database design, Python functions, parameterized SQL, staff and family-record management, and Matplotlib reporting. Future versions could add authenticated staff accounts, audited changes, encrypted storage, a graphical interface, and stronger validation after privacy and safeguarding requirements are reviewed.

## Viva questions

**1. Why keep parents/guardians in a separate table?**  
One parent or guardian can be linked to multiple children, and the same family record can be related to an application without repeating the person's details.

**2. What does a foreign key do?**  
It links a row to a related row and helps prevent references to missing records.

**3. Why use SQL placeholders?**  
They keep user-entered values separate from SQL instructions.

**4. What does Matplotlib do here?**  
It turns aggregate database results into charts.

**5. Does the application decide eligibility?**  
No. It tracks a human-reviewed workflow only.

**6. Why use fictional sample records?**  
The repository is public, so demo data avoids exposing children's or families' private information.
