-- Class 12 project: fictional orphanage-home management demo.
-- This schema tracks workflows; it does not decide legal or placement eligibility.
CREATE DATABASE IF NOT EXISTS orphanage_demo
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE orphanage_demo;

CREATE TABLE IF NOT EXISTS staff_members (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_code VARCHAR(20) NOT NULL UNIQUE,
    display_name VARCHAR(100) NOT NULL,
    role_name VARCHAR(60) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS children (
    child_id INT AUTO_INCREMENT PRIMARY KEY,
    child_code VARCHAR(24) NOT NULL UNIQUE,
    display_name VARCHAR(80) NOT NULL,
    date_of_birth DATE NULL,
    gender ENUM('Girl', 'Boy', 'Another identity', 'Prefer not to say')
        NOT NULL DEFAULT 'Prefer not to say',
    admission_date DATE NULL,
    school_grade VARCHAR(30) NULL,
    school_name VARCHAR(100) NULL,
    care_status ENUM('In care', 'Transitioned', 'Archived')
        NOT NULL DEFAULT 'In care',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_children_status (care_status),
    INDEX idx_children_gender (gender)
);

CREATE TABLE IF NOT EXISTS caregivers (
    caregiver_id INT AUTO_INCREMENT PRIMARY KEY,
    display_name VARCHAR(100) NOT NULL,
    relationship_label VARCHAR(50) NOT NULL,
    contact_reference VARCHAR(50) NOT NULL DEFAULT 'NOT RECORDED'
);

CREATE TABLE IF NOT EXISTS child_caregivers (
    child_id INT NOT NULL,
    caregiver_id INT NOT NULL,
    authority_review_status ENUM(
        'Not reviewed', 'Pending review', 'Reviewed by authorized person'
    ) NOT NULL DEFAULT 'Not reviewed',
    PRIMARY KEY (child_id, caregiver_id),
    FOREIGN KEY (child_id) REFERENCES children(child_id),
    FOREIGN KEY (caregiver_id) REFERENCES caregivers(caregiver_id)
);

CREATE TABLE IF NOT EXISTS admission_applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    application_code VARCHAR(24) NOT NULL UNIQUE,
    applicant_display_name VARCHAR(80) NOT NULL,
    age_years TINYINT UNSIGNED NULL,
    gender ENUM('Girl', 'Boy', 'Another identity', 'Prefer not to say')
        NOT NULL DEFAULT 'Prefer not to say',
    received_on DATE NOT NULL,
    referral_source VARCHAR(100) NOT NULL,
    parent_or_guardian_name VARCHAR(100) NOT NULL,
    parent_guardian_relationship VARCHAR(50) NOT NULL,
    parent_guardian_contact_reference VARCHAR(50) NOT NULL DEFAULT 'NOT RECORDED',
    status ENUM(
        'Pending review', 'Approved by reviewer', 'Referred', 'Closed'
    ) NOT NULL DEFAULT 'Pending review',
    reviewer_name VARCHAR(80) NULL,
    reviewer_note VARCHAR(255) NULL,
    decision_on DATE NULL,
    INDEX idx_applications_status (status),
    INDEX idx_applications_received (received_on)
);

CREATE TABLE IF NOT EXISTS review_criteria (
    criterion_id INT AUTO_INCREMENT PRIMARY KEY,
    criterion_code VARCHAR(30) NOT NULL UNIQUE,
    criterion_name VARCHAR(120) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT IGNORE INTO review_criteria (criterion_code, criterion_name) VALUES
('REFERRAL', 'Referral information recorded'),
('FAMILY_CONTEXT', 'Parent or guardian context reviewed'),
('DOCUMENTS', 'Required documentation checked under the local process'),
('SAFEGUARDING', 'Safeguarding review completed by an authorized person'),
('CARE_PLAN', 'Initial care and support needs discussed');

CREATE TABLE IF NOT EXISTS application_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT NOT NULL,
    criterion_id INT NOT NULL,
    review_status ENUM('Not started', 'In review', 'Reviewed')
        NOT NULL DEFAULT 'Not started',
    reviewer_name VARCHAR(80) NULL,
    reviewed_on DATE NULL,
    UNIQUE KEY uq_application_criterion (application_id, criterion_id),
    FOREIGN KEY (application_id) REFERENCES admission_applications(application_id)
        ON DELETE CASCADE,
    FOREIGN KEY (criterion_id) REFERENCES review_criteria(criterion_id)
);

CREATE TABLE IF NOT EXISTS education_records (
    education_id INT AUTO_INCREMENT PRIMARY KEY,
    child_id INT NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    school_grade VARCHAR(30) NOT NULL,
    attendance_percent DECIMAL(5,2) NOT NULL,
    result_percent DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (child_id) REFERENCES children(child_id),
    INDEX idx_education_year (academic_year)
);

CREATE TABLE IF NOT EXISTS donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_code VARCHAR(24) NOT NULL UNIQUE,
    display_name VARCHAR(100) NOT NULL,
    contact_reference VARCHAR(50) NOT NULL DEFAULT 'NOT RECORDED'
);

CREATE TABLE IF NOT EXISTS donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT NOT NULL,
    donated_on DATE NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    purpose VARCHAR(80) NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id),
    INDEX idx_donations_date (donated_on)
);

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    spent_on DATE NOT NULL,
    category VARCHAR(50) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    description VARCHAR(160) NOT NULL,
    INDEX idx_expenses_date (spent_on)
);

CREATE TABLE IF NOT EXISTS inventory_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_code VARCHAR(24) NOT NULL UNIQUE,
    item_name VARCHAR(80) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_name VARCHAR(20) NOT NULL,
    quantity_on_hand INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS inventory_movements (
    movement_id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    movement_type ENUM('IN', 'OUT') NOT NULL,
    quantity INT NOT NULL,
    moved_on DATE NOT NULL,
    purpose VARCHAR(120) NOT NULL,
    FOREIGN KEY (item_id) REFERENCES inventory_items(item_id),
    INDEX idx_inventory_moved_on (moved_on)
);
