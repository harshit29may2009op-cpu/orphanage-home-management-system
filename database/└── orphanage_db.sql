CREATE DATABASE IF NOT EXISTS orphanage_db;

USE orphanage_db;

-- ==============================
-- CHILDREN TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS children (
    child_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT,
    gender VARCHAR(10),
    admission_date DATE,
    class VARCHAR(20),
    school VARCHAR(100),
    health_status VARCHAR(100)
);

-- ==============================
-- STAFF TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    role VARCHAR(50),
    phone VARCHAR(15),
    salary DECIMAL(10,2)
);

-- ==============================
-- DONORS TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS donors (
    donor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100)
);

-- ==============================
-- DONATIONS TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS donations (
    donation_id INT PRIMARY KEY AUTO_INCREMENT,
    donor_id INT,
    amount DECIMAL(10,2),
    donation_date DATE,
    payment_mode VARCHAR(20),
    purpose VARCHAR(100),

    FOREIGN KEY (donor_id)
    REFERENCES donors(donor_id)
);

-- ==============================
-- EXPENSES TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    expense_date DATE,
    category VARCHAR(50),
    amount DECIMAL(10,2),
    description VARCHAR(150)
);

-- ==============================
-- EDUCATION TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS education (
    education_id INT PRIMARY KEY AUTO_INCREMENT,
    child_id INT,
    academic_year VARCHAR(20),
    class VARCHAR(20),
    attendance DECIMAL(5,2),
    percentage DECIMAL(5,2),

    FOREIGN KEY (child_id)
    REFERENCES children(child_id)
);

-- ==============================
-- INVENTORY TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS inventory (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(50),
    category VARCHAR(50),
    quantity INT,
    unit VARCHAR(20),
    last_updated DATE
);

-- ==============================
-- SAMPLE CHILDREN DATA
-- ==============================

INSERT INTO children
(name, age, gender, admission_date, class, school, health_status)
VALUES
('Aarav Sharma', 10, 'Male', '2023-04-12', '5',
 'Sunrise Public School', 'Healthy'),
('Ananya Verma', 12, 'Female', '2022-07-18', '7',
 'Green Valley School', 'Healthy'),
('Rohan Kumar', 14, 'Male', '2021-06-10', '9',
 'City Public School', 'Needs Regular Checkup'),
('Priya Singh', 11, 'Female', '2023-01-25', '6',
 'Sunrise Public School', 'Healthy'),
('Kabir Mehta', 15, 'Male', '2020-09-15', '10',
 'Modern School', 'Healthy');

-- ==============================
-- SAMPLE STAFF DATA
-- ==============================

INSERT INTO staff
(name, role, phone, salary)
VALUES
('Rajesh Kumar', 'Manager', '9876543210', 30000),
('Sunita Sharma', 'Caretaker', '9876543211', 22000),
('Meena Gupta', 'Teacher', '9876543212', 25000),
('Amit Verma', 'Cook', '9876543213', 18000);

-- ==============================
-- SAMPLE DONOR DATA
-- ==============================

INSERT INTO donors
(name, phone, email)
VALUES
('Rahul Foundation', '9811111111', 'rahul@example.com'),
('Neha Kapoor', '9822222222', 'neha@example.com'),
('Helping Hands NGO', '9833333333', 'helping@example.com');

-- ==============================
-- SAMPLE DONATION DATA
-- ==============================

INSERT INTO donations
(donor_id, amount, donation_date, payment_mode, purpose)
VALUES
(1, 25000, '2026-01-10', 'Online', 'Education'),
(2, 5000, '2026-02-15', 'UPI', 'Food'),
(3, 15000, '2026-03-20', 'Online', 'General'),
(1, 10000, '2026-04-12', 'UPI', 'Medical');

-- ==============================
-- SAMPLE EXPENSE DATA
-- ==============================

INSERT INTO expenses
(expense_date, category, amount, description)
VALUES
('2026-01-05', 'Food', 12000, 'Monthly groceries'),
('2026-01-15', 'Education', 8000, 'Books and stationery'),
('2026-02-10', 'Medical', 4500, 'Medical checkups'),
('2026-02-20', 'Clothing', 7000, 'Winter clothes'),
('2026-03-10', 'Food', 13000, 'Monthly groceries');

-- ==============================
-- SAMPLE EDUCATION DATA
-- ==============================

INSERT INTO education
(child_id, academic_year, class, attendance, percentage)
VALUES
(1, '2025-26', '5', 92.50, 86.00),
(2, '2025-26', '7', 95.00, 91.00),
(3, '2025-26', '9', 88.00, 78.00),
(4, '2025-26', '6', 94.00, 89.00),
(5, '2025-26', '10', 96.00, 93.00);

-- ==============================
-- SAMPLE INVENTORY DATA
-- ==============================

INSERT INTO inventory
(item_name, category, quantity, unit, last_updated)
VALUES
('Rice', 'Food', 50, 'kg', '2026-04-01'),
('Notebooks', 'Education', 100, 'pieces', '2026-04-02'),
('School Uniforms', 'Clothing', 25, 'sets', '2026-04-03'),
('First Aid Kits', 'Medical', 5, 'kits', '2026-04-04');
