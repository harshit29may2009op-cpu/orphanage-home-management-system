# Class 12 Computer Science Project Report

## Project title

Orphanage Home Management System — a Python and MySQL demonstration project

**Student:** ____________________  
**Class/section:** ____________________  
**School:** ____________________  
**Teacher:** ____________________

## Abstract

This project demonstrates how Python and MySQL can organize records for a fictional care home. It includes child profiles, parent or guardian context, an admission review checklist, education records, donations, expenses, and inventory. Matplotlib creates aggregate charts that help a reviewer understand application volume, donation trends, expenses, and the composition of the sample dataset.

The application records workflow information. It does not decide whether a child is eligible for placement. A qualified human must review each application and follow the applicable local process.

## Problem statement

Paper-based records can be difficult to search and summarize. A small database application can connect related records, reduce repeated data entry, flag low stock, and create simple summaries for planning.

## Objectives

1. Store related project records in MySQL tables connected with primary and foreign keys.
2. Use Python functions and parameterized SQL to add and search records.
3. Track admission-review checklist progress and a human-entered workflow status.
4. Record education, donation, expense, and inventory activity.
5. Generate at least three charts using Matplotlib.
6. Keep the public demonstration dataset fictional and use aggregate charts.

## Main modules

- **Child records:** add, search, and list demo profiles.
- **Admissions:** record a referral, parent/guardian context, and application status.
- **Review checklist:** track whether configured review items are not started, in review, or reviewed. This is not an eligibility score.
- **Education:** record grade, attendance, and result percentage.
- **Donations and expenses:** record amounts, dates, and categories for summaries.
- **Inventory:** record incoming and outgoing stock and show low-stock items.
- **Charts:** create four PNG charts from aggregate MySQL queries.

## Database design

The schema uses separate tables for children, caregivers, their relationship, applications, review criteria, review progress, education, donors, donations, expenses, inventory items, inventory movements, and staff. Primary keys identify rows; foreign keys connect related records. This avoids storing every detail in one large table and makes summary queries possible.

## Charts

1. **Children by recorded gender:** a count by category for the synthetic dataset. Gender is not used in eligibility or admission decisions.
2. **Application workflow:** counts of applications by their human-entered status.
3. **Donations by month:** monthly totals from fictional donation records.
4. **Expenses by category:** totals grouped by expense category.

## Privacy and fairness choices

- Public sample records use DEMO labels and contain no real child or family identities or phone numbers.
- The charts show totals and categories rather than names.
- The program does not use gender to accept or reject applications.
- The checklist records review progress only. Local rules and an authorized human review are outside the program.
- This project is for learning; it has no user authentication, role-based access, encryption, or production safeguards. Do not enter real personal or safeguarding information.

## Conclusion and future scope

The project shows how a relational database, Python menu, parameterized queries, and Matplotlib reports can support a record-keeping workflow. Future versions could add authenticated staff accounts, audited changes, encrypted storage, stronger validation, exportable reports, and a graphical interface after privacy and safeguarding requirements are reviewed.

## Viva questions

**1. What is a primary key?**  
A column, or set of columns, that uniquely identifies each row in a table.

**2. Why use foreign keys?**  
They link related tables and help prevent records from referring to missing parent rows.

**3. Why are query placeholders used?**  
They separate user-entered values from SQL text and help avoid SQL injection errors.

**4. What does Matplotlib do in this project?**  
It turns aggregate database query results into charts.

**5. Does the program automatically decide eligibility?**  
No. It records checklist progress and a human-entered status only.

**6. Why use synthetic data?**  
The repository is public, so fictional data avoids exposing real children's or families' private information.
