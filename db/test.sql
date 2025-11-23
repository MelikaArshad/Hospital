-- =================================================
-- TEST DATA FOR HOSPITAL MEDICAL REPORT SYSTEM
-- Safe to run multiple times (uses INSERT OR IGNORE)
-- =================================================

-- Departments
INSERT OR IGNORE INTO departments (department_id, department_name, department_controller) VALUES
(1, 'Cardiology', 'Dr. Ali Ahmadi'),
(2, 'General Surgery', 'Dr. Sara Rezaei'),
(3, 'Internal Medicine', 'Dr. Reza Mohammadi'),
(4, 'Pediatrics', 'Dr. Maryam Hosseini'),
(5, 'Obstetrics & Gynecology', 'Dr. Fatemeh Sharifi'),
(6, 'Emergency Department', 'Dr. Hossein Karimi'),
(7, 'Neurology', 'Dr. Nima Javadi'),
(8, 'Orthopedics', 'Dr. Kaveh Yazdani');

-- Doctors
INSERT OR IGNORE INTO doctor (doctor_id, full_name, department_controller, father_name, national_code, personal_id_no, degree, birth_date, age, phone_number, address, username, password) VALUES
(1, 'Dr. Ali Ahmadi', 'Cardiology', 'Hassan', '0023456789', 'A10012001', 'Cardiologist (Fellowship)', '1965-06-05', '59', '+989123456789', 'Tehran, Azadi St.', 'dr_ahmadi', 'pass123'),
(2, 'Dr. Sara Rezaei', 'General Surgery', 'Mohammad', '0056789123', 'B10012002', 'General Surgeon', '1970-09-14', '54', '+989129876543', 'Tehran, Vanak Sq.', 'dr_rezaei', 'pass123'),
(3, 'Dr. Reza Mohammadi', 'Internal Medicine', 'Akbar', '0011122233', 'C10012003', 'Internist', '1968-02-19', '56', '+989351234567', 'Tehran, Saadat Abad', 'dr_mohammadi', 'pass123'),
(4, 'Dr. Maryam Hosseini', 'Pediatrics', 'Hossein', '0088899900', 'D10012004', 'Pediatrician (Subspecialist)', '1972-07-30', '52', '+989123459876', 'Tehran, Niavaran', 'dr_hosseini', 'pass123');

-- Hospital Staff
INSERT OR IGNORE INTO staff (id, full_name, father_name, national_code, personal_id_no, degree, birth_date, age, phone_number, address, username, password, ward, role) VALUES
(1, 'Zahra Karimi', 'Ali', '0034567890', 'N10001', 'B.Sc. Nursing', '1975-06-20', '49', '+989127654321', 'Tehran, Shahrak-e Gharb', 'nurse_zahra', 'n123', 'Cardiology', 'Head Nurse'),
(2, 'Mohammad Sharifi', 'Hassan', '0045678901', 'N10002', 'Emergency Medical Technician', '1978-11-15', '46', '+989359876543', 'Tehran, Pasdaran', 'tech_mohammad', 'n123', 'Emergency', 'EMT'),
(3, 'Fatemeh Nouri', 'Reza', '0078901234', 'N10003', 'Midwifery', '1980-04-28', '44', '+989128765432', 'Tehran, Tajrish', 'midwife_fatemeh', 'n123', 'Obstetrics', 'Midwife'),
(4, 'Hassan Rezaei', 'Akbar', '0098765432', 'N10004', 'Operating Room Technician', '1976-02-25', '48', '+989358765432', 'Tehran, Narmak', 'or_hassan', 'n123', 'General Surgery', 'OR Technician');

-- Sample Patients (for Medical Reports)
INSERT OR IGNORE INTO patient (id, full_name, father_name, national_code, birth_date, phone_number, address, entry_date, illness, doctor_id, ward) VALUES
(1, 'Ahmad Mohammadi', 'Hossein', '1234567890', '1981-08-30', '+989123456780', 'Tehran, Enghelab St.', '2024-11-01', 'Unstable Angina', 1, 'Cardiology'),
(2, 'Maryam Ahmadi', 'Ali', '2345678901', '1996-05-17', '+989351234567', 'Tehran, Vanak', '2024-11-05', 'Acute Appendicitis', 2, 'General Surgery'),
(3, 'Reza Hosseini', 'Mohammad', '3456789012', '2011-01-28', '+989129876543', 'Tehran, Niavaran', '2024-11-10', 'Pneumonia', 3, 'Pediatrics'),
(4, 'Zainab Rezaei', 'Hassan', '4567890123', '2019-12-20', '+989358765432', 'Tehran, Saadat Abad', '2024-11-12', 'Viral Fever & Bronchiolitis', 4, 'Pediatrics'),
(5, 'Fatemeh Sharifi', 'Akbar', '5678901234', '1993-09-09', '+989127654321', 'Tehran, Shahrak-e Gharb', '2024-10-28', 'Normal Delivery', 2, 'Obstetrics & Gynecology'),
(6, 'Hossein Javadi', 'Reza', '6789012345', '1978-03-15', '+989112345678', 'Tehran, Jordan', '2024-11-18', 'Acute Stroke', 1, 'Neurology'),
(7, 'Niloofar Yazdani', 'Kaveh', '7890123456', '1985-07-22', '+989134567890', 'Tehran, Elahieh', '2024-11-20', 'Fractured Femur', 2, 'Orthopedics');
