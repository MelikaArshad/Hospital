-- ATTACH DATABASE 'db/hospital.db' AS hospital;

-- ============================================
-- DATABASE SCHEMA FOR HOSPITAL SYSTEM
-- Exact match with Model __init__ parameters
-- ============================================

-- Departments: (department_id,department_name,department_controller)
create table if not exists departments(
    department_id integer primary key autoincrement,
    department_name text not null,
    department_controller text not null
);

-- Doctors: (doctor_id,full_name ,department_controller,father_name, national_code, personal_id_no, degree, birth_date, age,
--                  phone_number,address, username, password)
create table if not exists doctors(
    doctor_id integer primary key autoincrement,
    full_name text not null,
    department_controller text not null,
    father_name text not null,
    national_code integer not null,
    personal_id_no integer not null,
    degree text not null,
    birth_date text not null,
    age integer not null,
    phone_number text not null,
    address text not null,
    username text not null,
    password text not null
);

-- Patients: (unit_no, full_name, father_name, national_code, birth_date,phone_number, age, height, weight,
--                  attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text="")
create table if not exists patients(
    unit_no integer primary key autoincrement,
    full_name text not null,
    father_name text not null,
    national_code integer not null,
    birth_date text not null,
    phone_number text not null,
    age integer not null,
    height integer not null ,
    weight integer not null,
    attending_physician text not null,
    kind_of_ad text not null,
    date_of_admission text not null,
    ward text not null,
    room integer  not null,
    bed integer not null,
    notes_text text not null default ''
);

-- staffs: (staff_id, full_name, father_name, national_code, personal_id_no, degree, birth_date, age, phone_number,
--                  address, username, password, ward, role)
create table if not exists staffs (
    staff_id integer primary key autoincrement,
    full_name text not null,
    father_name text not null,
    national_code integer not null,
    personal_id_no integer not null,
    degree text not null,
    birth_date text not null,
    age integer not null,
    phone_number text not null,
    address text not null,
    username text not null,
    password text not null,
    ward text not null,
    role text not null
);
-- medical_records: (record_id,unit_no,full_name,doctor_name,staff_name,department_name,session_type,description,medication,nursing_care,lab_tests,services,total_amount,payment_status,date_of_admission)
create table if not exists medical_records (
    record_id integer primary key autoincrement,
    unit_no integer not null,
    full_name text not null,
    doctor_name text not null,
    staff_name text not null,
    department_name text not null,
    session_type text not null,
    description text not null,
    medication text not null,
    nursing_care text not null,
    lab_tests text not null,
    services text not null,
    total_amount integer not null,
    payment_status text not null ,
    date_of_admission text not null
);