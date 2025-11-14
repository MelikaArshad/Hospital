import sqlite3
from model import Patient


class PatientRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./db/hospital_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, patient):
        self.connect()
        self.cursor.execute("insert into patients (full_name, father_name, national_code, birth_date,phone_number, age, height, weight,attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            [patient.full_name, patient.father_name, patient.national_code, patient.birth_date,patient.phone_number, patient.age, patient.height, patient.weight,
                 patient.attending_physician, patient.kind_of_ad, patient.date_of_admission, patient.ward, patient.room,patient.bed, patient.notes_text])
        patient.id = self.cursor.lastrowid
        self.connection.commit()
        return patient

    def update(self, patient):
        self.connect()
        self.cursor.execute("update patients set full_name=?, father_name=?, national_code=?, birth_date=?,phone_number=?, age=?, height=?, weight=?,attending_physician=?, kind_of_ad=?, date_of_admission=?, ward=?, room=?, bed=?, notes_text=? where id=?",
                            [patient.unit_no,patient.full_name, patient.father_name, patient.national_code, patient.birth_date,patient.phone_number, patient.age, patient.height, patient.weight,
                 patient.attending_physician, patient.kind_of_ad, patient.date_of_admission, patient.ward, patient.room,patient.bed, patient.notes_text ])
        self.connection.commit()
        self.disconnect()
        return patient

    def delete(self, unit_no):
        self.connect()
        self.cursor.execute("delete from patients where unit_no=?",
                            [unit_no])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from patients")
        patient_list = [Patient(*patient) for patient in self.cursor.fetchall()]
        self.disconnect()
        return patient_list

    def find_by_unit_no(self, unit_no):
        self.connect()
        self.cursor.execute("select * from patients where unit_no=?", [unit_no])
        patient = self.cursor.fetchone()
        self.disconnect()
        if patient:
            return Patient(*patient)
        return None


    def find_by_name(self, full_name):
        self.connect()
        self.cursor.execute("select * from patients where full_name like ?", [full_name + "%"])
        patient_list = [Patient(*patient) for patient in self.cursor.fetchall()]
        self.disconnect()
        return patient_list


    def find_by_national_code(self, national_code):
        self.connect()
        self.cursor.execute("select * from patients where national_code like ?", [national_code + "%"])
        patient_list = [Patient(*patient) for patient in self.cursor.fetchall()]
        self.disconnect()
        return patient_list


