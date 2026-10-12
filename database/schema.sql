-- MySQL setup for the Class 12 project
CREATE DATABASE IF NOT EXISTS orphanage_class12_demo_v3;
USE orphanage_class12_demo_v3;

CREATE TABLE IF NOT EXISTS children (
    child_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(20),
    school_class INT,
    admission_date DATE,
    care_status VARCHAR(20) DEFAULT 'In Care',
    adoption_legal_status VARCHAR(40) DEFAULT 'Not Assessed or Not Declared'
);

CREATE TABLE IF NOT EXISTS guardians (
    guardian_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    phone VARCHAR(30),
    address VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS child_guardians (
    link_id INT AUTO_INCREMENT PRIMARY KEY,
    child_id INT NOT NULL,
    guardian_id INT NOT NULL,
    relationship VARCHAR(30),
    FOREIGN KEY (child_id) REFERENCES children(child_id),
    FOREIGN KEY (guardian_id) REFERENCES guardians(guardian_id)
);

CREATE TABLE IF NOT EXISTS applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_name VARCHAR(60) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(20),
    guardian_id INT NOT NULL,
    relationship VARCHAR(30),
    application_status VARCHAR(25) DEFAULT 'Under Review',
    FOREIGN KEY (guardian_id) REFERENCES guardians(guardian_id)
);

CREATE TABLE IF NOT EXISTS application_reviews (
    application_id INT PRIMARY KEY,
    care_need_checked VARCHAR(20) DEFAULT 'Not checked',
    documents_checked VARCHAR(20) DEFAULT 'Not checked',
    guardian_contacted VARCHAR(20) DEFAULT 'Not checked',
    decision VARCHAR(25) DEFAULT 'Pending',
    FOREIGN KEY (application_id) REFERENCES applications(application_id)
);

CREATE TABLE IF NOT EXISTS adoptive_applications (
    applicant_id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_name VARCHAR(60) NOT NULL,
    applicant_age INT NOT NULL,
    applicant_type VARCHAR(20),
    marital_status VARCHAR(30),
    spouse_consent VARCHAR(20),
    phone VARCHAR(30),
    address VARCHAR(100),
    occupation VARCHAR(50),
    family_children INT,
    submitted_date DATE,
    documents_status VARCHAR(20) DEFAULT 'Pending',
    home_study_status VARCHAR(20) DEFAULT 'Pending',
    eligibility_status VARCHAR(30) DEFAULT 'Pending',
    application_status VARCHAR(30) DEFAULT 'Submitted'
);

CREATE TABLE IF NOT EXISTS adoption_cases (
    adoption_id INT AUTO_INCREMENT PRIMARY KEY,
    child_id INT NOT NULL UNIQUE,
    applicant_id INT NOT NULL,
    order_date DATE NOT NULL,
    order_reference VARCHAR(60) NOT NULL,
    FOREIGN KEY (child_id) REFERENCES children(child_id),
    FOREIGN KEY (applicant_id) REFERENCES adoptive_applications(applicant_id)
);

CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    job_title VARCHAR(40),
    phone VARCHAR(30),
    work_status VARCHAR(20) DEFAULT 'Active'
);

CREATE TABLE IF NOT EXISTS donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_name VARCHAR(60),
    donation_date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    purpose VARCHAR(60)
);

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    category VARCHAR(40) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    details VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS inventory (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    reorder_level INT NOT NULL
);

-- Aggregate-only fictional data. This table has no child ID or name.
CREATE TABLE IF NOT EXISTS support_summary (
    summary_id INT AUTO_INCREMENT PRIMARY KEY,
    support_category VARCHAR(80) NOT NULL,
    child_count INT NOT NULL
);
