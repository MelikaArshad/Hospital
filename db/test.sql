-- =================================================
-- TEST DATA FOR HOSPITAL MEDICAL REPORT SYSTEM
-- Safe to run multiple times (uses INSERT OR IGNORE)
-- =================================================

-- Doctors
INSERT OR IGNORE INTO doctors (id, full_name, father_name, national_code, birth_date, personal_id_no, degree, phone_number, address, username, password) VALUES
(1, 'Dr. Reza Ahmadi', 'Hassan', '0012345678', '1968-05-12', 'A123456789', 'Cardiologist', '+989123456789', 'Tehran, Valiasr St.', 'dr_reza', 'pass123'),
(2, 'Dr. Sara Hosseini', 'Mohammad', '0012345679', '1975-08-20', 'B987654321', 'General Surgeon', '+989129876543', 'Tehran, Jordan Ave.', 'dr_sara', 'pass123'),
(3, 'Dr. Ali Mohammadi', 'Akbar', '0012345680', '1972-03-15', 'C112233445', 'Pediatrician', '+989351234567', 'Tehran, Saadat Abad', 'dr_ali', 'pass123'),
(4, 'Dr. Maryam Karimi', 'Reza', '0012345681', '1980-11-30', 'D556677889', 'Internal Medicine', '+989123498765', 'Tehran, Niavaran', 'dr_maryam', 'pass123');

-- Staffs
INSERT OR IGNORE INTO staffs (id, full_name, father_name, national_code, personal_id_no, degree, birth_date, age, phone_number, address, username, password, ward, role) VALUES
(1, 'Zahra Rahimi', 'Ali', '0034567890', 'N1001', 'B.Sc Nursing', '1985-06-10', '39', '+989127654321', 'Tehran, Shahrak Gharb', 'zahra_nurse', 'n123', 'Cardiology', 'Head Nurse'),
(2, 'Mohammad Jafari', 'Hossein', '0034567891', 'N1002', 'Emergency Technician', '1988-09-18', '36', '+989359876543', 'Tehran, Pasdaran', 'mohammad_emt', 'n123', 'Emergency', 'EMT Specialist'),
(3, 'Fatemeh Nouri', 'Reza', '0034567892', 'N1003', 'Midwifery', '1990-02-25', '34', '+989128765432', 'Tehran, Tajrish', 'fatemeh_midwife', 'n123', 'Obstetrics', 'Senior Midwife'),
(4, 'Hassan Yazdani', 'Akbar', '0034567893', 'N1004', 'Lab Technician', '1987-12-05', '37', '+989358765432', 'Tehran, Narmak', 'hassan_lab', 'n123', 'Laboratory', 'Lab Supervisor');

-- Patients
INSERT OR IGNORE INTO patients (unit_no, full_name, father_name, national_code, birth_date, phone_number, height, weight, attending_physician, kind_of_admission, ward, room, bed) VALUES
(1001, 'Ahmad Rezaei', 'Hossein', 1234567890, '1980-07-22', '+989123456780', 178, 85, 'Dr. Reza Ahmadi', 'Emergency', 'Cardiology', '201', 'A1'),
(1002, 'Maryam Ahmadi', 'Ali', 2345678901, '1995-04-18', '+989351234567', 165, 58, 'Dr. Sara Hosseini', 'Surgical', 'General Surgery', '305', 'B2'),
(1003, 'Mohammad Hossein', 'Reza', 3456789012, '2015-11-30', '+989129876543', 112, 28, 'Dr. Ali Mohammadi', 'Outpatient', 'Pediatrics', '102', 'C3'),
(1004, 'Zahra Karimi', 'Hasan', 4567890123, '1988-09-14', '+989358765432', 170, 62, 'Dr. Maryam Karimi', 'Referral', 'Internal Medicine', '408', 'D1');

-- Medical Records
INSERT OR IGNORE INTO medical_records (
    record_id, unit_no, full_name_doctor, staff_name, department_name, session_type,
    description, nursing_care, lab_tests, total_amount, date_of_admission
) VALUES
(1, 1001, 'Dr. Reza Ahmadi', 'Zahra Rahimi', 'Cardiology', 'Follow-up Visit',
 'Patient reports chest pain on exertion. ECG shows ST changes. Recommended angiography.',
 'Vital signs stable. IV access maintained. Oxygen 2L/min via nasal cannula.',
 'Troponin: 0.8, CK-MB: 45, CBC normal, Lipid profile pending', 2850000, '2025-11-20'),
 
(2, 1002, 'Dr. Sara Hosseini', 'Mohammad Jafari', 'General Surgery', 'Post-Op Day 1',
 'Laparoscopic appendectomy performed successfully. No complications.',
 'Wound dressing changed. Pain managed with IV analgesics. Mobilization started.',
 'WBC: 12.4, Hb: 13.1, CRP: 68', 5400000, '2025-11-18'),
 
(3, 1003, 'Dr. Ali Mohammadi', 'Fatemeh Nouri', 'Pediatrics', 'Acute Visit',
 '5-year-old with high fever and cough. Diagnosed with viral pneumonia.',
 'Nebulization with salbutamol. Hydration maintained. Paracetamol given.',
 'Chest X-ray: bilateral infiltrates, RSV positive', 1800000, '2025-11-22'),
 
(4, 1004, 'Dr. Maryam Karimi', 'Hassan Yazdani', 'Internal Medicine', 'Consultation',
 'Patient with uncontrolled diabetes and fatigue. Adjusted insulin regimen.',
 'Blood sugar monitoring q4h. Diet consultation done.',
 'HbA1c: 9.8, Fasting BS: 210, Kidney function normal', 1200000, '2025-11-19');
