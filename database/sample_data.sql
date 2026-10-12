-- All names and records below are fictional examples, not real children or families.
-- Juvenile-justice support is an anonymous separate count with no child IDs.
USE orphanage_class12_demo_v3;

INSERT INTO children (name, age, gender, school_class, admission_date, care_status, adoption_legal_status) VALUES
('Aarav Sharma', 5, 'Girl', 1, '2022-01-10', 'Adopted', 'Legally Free for Adoption'),
('Ananya Verma', 6, 'Boy', 2, '2022-02-10', 'In Care', 'Not Assessed or Not Declared'),
('Vihaan Patel', 7, 'Not recorded', 3, '2022-03-10', 'In Care', 'Not Assessed or Not Declared'),
('Saanvi Gupta', 8, 'Girl', 4, '2022-04-10', 'In Care', 'Not Assessed or Not Declared'),
('Arjun Mehta', 9, 'Boy', 5, '2022-05-10', 'In Care', 'Not Assessed or Not Declared'),
('Diya Nair', 10, 'Not recorded', 6, '2022-06-10', 'In Care', 'Not Assessed or Not Declared'),
('Kabir Singh', 11, 'Girl', 7, '2022-07-10', 'Adopted', 'Legally Free for Adoption'),
('Myra Iyer', 12, 'Boy', 8, '2022-08-10', 'In Care', 'Not Assessed or Not Declared'),
('Advik Rao', 13, 'Not recorded', 9, '2022-09-10', 'In Care', 'Not Assessed or Not Declared'),
('Aadhya Joshi', 14, 'Girl', 10, '2022-10-10', 'In Care', 'Not Assessed or Not Declared'),
('Ishaan Kapoor', 15, 'Boy', 11, '2022-11-10', 'In Care', 'Not Assessed or Not Declared'),
('Kiara Das', 16, 'Not recorded', 12, '2022-12-10', 'In Care', 'Not Assessed or Not Declared'),
('Reyansh Khanna', 17, 'Girl', 1, '2022-01-10', 'Adopted', 'Legally Free for Adoption'),
('Tara Malhotra', 5, 'Boy', 2, '2022-02-10', 'In Care', 'Not Assessed or Not Declared'),
('Atharv Mishra', 6, 'Not recorded', 3, '2022-03-10', 'In Care', 'Not Assessed or Not Declared'),
('Meera Menon', 7, 'Girl', 4, '2022-04-10', 'In Care', 'Not Assessed or Not Declared'),
('Rohan Sethi', 8, 'Boy', 5, '2022-05-10', 'In Care', 'Not Assessed or Not Declared'),
('Navya Reddy', 9, 'Not recorded', 6, '2022-06-10', 'In Care', 'Not Assessed or Not Declared'),
('Dhruv Jain', 10, 'Girl', 7, '2022-07-10', 'In Care', 'Not Assessed or Not Declared'),
('Pari Shah', 11, 'Boy', 8, '2022-08-10', 'In Care', 'Not Assessed or Not Declared'),
('Kian Bose', 12, 'Not recorded', 9, '2022-09-10', 'In Care', 'Not Assessed or Not Declared'),
('Ira Chawla', 13, 'Girl', 10, '2022-10-10', 'In Care', 'Not Assessed or Not Declared'),
('Neel Bhatia', 14, 'Boy', 11, '2022-11-10', 'In Care', 'Not Assessed or Not Declared'),
('Zoya Khan', 15, 'Not recorded', 12, '2022-12-10', 'In Care', 'Not Assessed or Not Declared'),
('Samar Roy', 16, 'Girl', 1, '2022-01-10', 'In Care', 'Not Assessed or Not Declared'),
('Vanya Pillai', 17, 'Boy', 2, '2022-02-10', 'In Care', 'Not Assessed or Not Declared'),
('Omkar Desai', 5, 'Not recorded', 3, '2022-03-10', 'In Care', 'Not Assessed or Not Declared'),
('Pihu Banerjee', 6, 'Girl', 4, '2022-04-10', 'In Care', 'Not Assessed or Not Declared'),
('Yash Thakur', 7, 'Boy', 5, '2022-05-10', 'In Care', 'Not Assessed or Not Declared'),
('Amara Fernandes', 8, 'Not recorded', 6, '2022-06-10', 'In Care', 'Not Assessed or Not Declared'),
('Krish Dutta', 9, 'Girl', 7, '2022-07-10', 'In Care', 'Not Assessed or Not Declared'),
('Siya Sood', 10, 'Boy', 8, '2022-08-10', 'In Care', 'Not Assessed or Not Declared'),
('Devika Naidu', 11, 'Not recorded', 9, '2022-09-10', 'In Care', 'Not Assessed or Not Declared'),
('Ayaan Kulkarni', 12, 'Girl', 10, '2022-10-10', 'In Care', 'Not Assessed or Not Declared'),
('Ria Chatterjee', 13, 'Boy', 11, '2022-11-10', 'In Care', 'Not Assessed or Not Declared');

INSERT INTO guardians (name, phone, address) VALUES
('Asha Sharma', 'DEMO-PHONE-01', 'Demo district'),
('Rajesh Verma', 'DEMO-PHONE-02', 'Demo district'),
('Sunita Patel', 'DEMO-PHONE-03', 'Demo district'),
('Manoj Gupta', 'DEMO-PHONE-04', 'Demo district'),
('Farida Mehta', 'DEMO-PHONE-05', 'Demo district'),
('Joseph Nair', 'DEMO-PHONE-06', 'Demo district'),
('Kavita Singh', 'DEMO-PHONE-07', 'Demo district'),
('Suresh Iyer', 'DEMO-PHONE-08', 'Demo district'),
('Rekha Rao', 'DEMO-PHONE-09', 'Demo district'),
('Amit Joshi', 'DEMO-PHONE-10', 'Demo district'),
('Farah Kapoor', 'DEMO-PHONE-11', 'Demo district'),
('Anand Das', 'DEMO-PHONE-12', 'Demo district'),
('Meena Khanna', 'DEMO-PHONE-13', 'Demo district'),
('Sanjay Malhotra', 'DEMO-PHONE-14', 'Demo district'),
('Pushpa Mishra', 'DEMO-PHONE-15', 'Demo district'),
('Thomas Menon', 'DEMO-PHONE-16', 'Demo district'),
('Neelam Reddy', 'DEMO-PHONE-17', 'Demo district'),
('Vinod Jain', 'DEMO-PHONE-18', 'Demo district');

INSERT INTO child_guardians (child_id, guardian_id, relationship) VALUES
(1, 1, 'Parent/Guardian'),
(2, 2, 'Parent/Guardian'),
(3, 3, 'Parent/Guardian'),
(4, 4, 'Parent/Guardian'),
(5, 5, 'Parent/Guardian'),
(6, 6, 'Parent/Guardian'),
(7, 7, 'Parent/Guardian'),
(8, 8, 'Parent/Guardian'),
(9, 9, 'Parent/Guardian'),
(10, 10, 'Parent/Guardian'),
(11, 11, 'Parent/Guardian'),
(12, 12, 'Parent/Guardian'),
(13, 13, 'Parent/Guardian'),
(14, 14, 'Parent/Guardian'),
(15, 15, 'Parent/Guardian'),
(16, 16, 'Parent/Guardian'),
(17, 17, 'Parent/Guardian'),
(18, 18, 'Parent/Guardian'),
(19, 1, 'Parent/Guardian'),
(20, 2, 'Parent/Guardian'),
(21, 3, 'Parent/Guardian'),
(22, 4, 'Parent/Guardian'),
(23, 5, 'Parent/Guardian'),
(24, 6, 'Parent/Guardian'),
(25, 7, 'Parent/Guardian'),
(26, 8, 'Parent/Guardian'),
(27, 9, 'Parent/Guardian'),
(28, 10, 'Parent/Guardian'),
(29, 11, 'Parent/Guardian'),
(30, 12, 'Parent/Guardian'),
(31, 13, 'Parent/Guardian'),
(32, 14, 'Parent/Guardian'),
(33, 15, 'Parent/Guardian'),
(34, 16, 'Parent/Guardian'),
(35, 17, 'Parent/Guardian');

INSERT INTO staff (name, job_title, phone, work_status) VALUES
('Meera Kulkarni', 'Caregiver', 'DEMO-STAFF-01', 'Active'),
('Rakesh Sethi', 'Teacher', 'DEMO-STAFF-02', 'Active'),
('Farah Khan', 'Cook', 'DEMO-STAFF-03', 'Active'),
('Joseph Fernandes', 'Nurse', 'DEMO-STAFF-04', 'Active'),
('Kavita Rao', 'Administrator', 'DEMO-STAFF-05', 'Active'),
('Arvind Iyer', 'Caregiver', 'DEMO-STAFF-06', 'Active'),
('Sunita Bose', 'Account Assistant', 'DEMO-STAFF-07', 'On Leave'),
('Nitin Shah', 'Teacher', 'DEMO-STAFF-08', 'Active');

INSERT INTO applications (applicant_name, age, gender, guardian_id, relationship, application_status) VALUES
('Anita Das', 7, 'Girl', 1, 'Parent/Guardian', 'Under Review'),
('Rahul Mehta', 8, 'Boy', 2, 'Parent/Guardian', 'Under Review'),
('Yasmin Ali', 9, 'Not recorded', 3, 'Parent/Guardian', 'Received'),
('Karan Shah', 10, 'Girl', 4, 'Parent/Guardian', 'Under Review'),
('Pooja Kapoor', 11, 'Boy', 5, 'Parent/Guardian', 'Closed'),
('Imran Khan', 12, 'Not recorded', 6, 'Parent/Guardian', 'Received'),
('Leela Menon', 13, 'Girl', 7, 'Parent/Guardian', 'Under Review'),
('Mohit Rao', 14, 'Boy', 8, 'Parent/Guardian', 'Closed'),
('Shreya Dutta', 15, 'Not recorded', 9, 'Parent/Guardian', 'Received'),
('Faisal Fernandes', 16, 'Girl', 10, 'Parent/Guardian', 'Under Review');

INSERT INTO application_reviews (application_id, care_need_checked, documents_checked, guardian_contacted, decision) VALUES
(1, 'Not checked', 'Not checked', 'Not checked', 'Pending'),
(2, 'Yes', 'Not checked', 'Yes', 'Pending'),
(3, 'Yes', 'Yes', 'Yes', 'Eligible'),
(4, 'Not checked', 'Not checked', 'Not checked', 'Pending'),
(5, 'Yes', 'Not checked', 'Yes', 'Not eligible'),
(6, 'Yes', 'Yes', 'Yes', 'Eligible'),
(7, 'Not checked', 'Not checked', 'Not checked', 'Pending'),
(8, 'Yes', 'Not checked', 'Yes', 'Not eligible'),
(9, 'Yes', 'Yes', 'Yes', 'Eligible'),
(10, 'Not checked', 'Not checked', 'Not checked', 'Pending');

INSERT INTO adoptive_applications (applicant_name, applicant_age, applicant_type, marital_status, spouse_consent, phone, address, occupation, family_children, submitted_date, documents_status, home_study_status, eligibility_status, application_status) VALUES
('Nisha Menon', 38, 'Couple', 'Married', 'Yes', 'DEMO-ADOPTER-01', 'Demo district', 'Teacher', 0, '2023-01-15', 'Checked', 'Complete', 'Verified Eligible', 'Finalized'),
('Arjun Bose', 42, 'Single', 'Single', 'Not applicable', 'DEMO-ADOPTER-02', 'Demo district', 'Doctor', 1, '2024-02-11', 'Checked', 'Complete', 'Verified Eligible', 'Finalized'),
('Rukmini Sethi', 40, 'Couple', 'Married', 'Yes', 'DEMO-ADOPTER-03', 'Demo district', 'Business', 0, '2025-03-12', 'Checked', 'Complete', 'Verified Eligible', 'Finalized'),
('Milan Shah', 36, 'Couple', 'Married', 'Yes', 'DEMO-ADOPTER-04', 'Demo district', 'Engineer', 0, '2025-06-05', 'Pending', 'Pending', 'Pending', 'In Review'),
('Farzana Khan', 45, 'Single', 'Widowed', 'Not applicable', 'DEMO-ADOPTER-05', 'Demo district', 'Nurse', 2, '2025-09-21', 'Pending', 'Pending', 'Pending', 'Submitted');

INSERT INTO adoption_cases (child_id, applicant_id, order_date, order_reference) VALUES
(1, 1, '2023-04-15', 'DEMO-ORDER-2023-001'),
(7, 2, '2024-06-20', 'DEMO-ORDER-2024-001'),
(13, 3, '2025-08-11', 'DEMO-ORDER-2025-001');

INSERT INTO donations (donor_name, donation_date, amount, purpose) VALUES
('Rohan Gupta', '2025-01-15', 2500, 'General support'),
('Meera Thomas', '2025-02-15', 3200, 'Books support'),
('Irfan Ansari', '2025-03-15', 2800, 'General support'),
('Kavita Desai', '2025-04-15', 4100, 'Books support'),
('Sanjay Pillai', '2025-05-15', 3500, 'General support'),
('Leena Roy', '2025-06-15', 5000, 'Books support'),
('Aditya Sen', '2025-07-15', 4600, 'General support'),
('Nandita Bose', '2025-08-15', 3900, 'Books support'),
('Farhan Ali', '2025-09-15', 5200, 'General support'),
('Deepa Nair', '2025-10-15', 4800, 'Books support'),
('Joseph Mathew', '2025-11-15', 6100, 'General support'),
('Priya Kulkarni', '2025-12-15', 7000, 'Books support');

INSERT INTO expenses (expense_date, category, amount, details) VALUES
('2025-01-20', 'Food', 18000, 'Demo monthly food supplies'),
('2025-02-12', 'Education', 7200, 'Demo books and stationery'),
('2025-03-09', 'Health', 5400, 'Demo clinic and medicine costs'),
('2025-04-14', 'Utilities', 8300, 'Demo electricity and water'),
('2025-05-18', 'Clothing', 6100, 'Demo seasonal clothing'),
('2025-06-22', 'Food', 19400, 'Demo monthly food supplies'),
('2025-07-12', 'Education', 6800, 'Demo school supplies'),
('2025-08-16', 'Health', 4900, 'Demo clinic and medicine costs'),
('2025-09-11', 'Utilities', 8700, 'Demo electricity and water'),
('2025-10-19', 'Food', 20100, 'Demo monthly food supplies');

INSERT INTO inventory (item_name, quantity, reorder_level) VALUES
('Rice bags', 18, 8),
('Notebooks', 75, 30),
('Pencils', 110, 40),
('First-aid kits', 4, 2),
('Blankets', 42, 15),
('Soap packs', 36, 12),
('School books', 52, 20),
('Sports balls', 6, 3);

INSERT INTO support_summary (support_category, child_count) VALUES
('Children currently in care (home sample)', 32),
('Separate juvenile justice support cases (anonymous demo)', 2);