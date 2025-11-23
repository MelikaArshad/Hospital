
import sqlite3
from model.medical_record import MedicalRecord
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "db/hospital.db")

class MedicalRecordRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, record: MedicalRecord) :
        self.connect()
        self.cursor.execute("insert into medical_records (unit_no, full_name, doctor_name, staff_name, department_name,session_type, description, medications, nursing_care,lab_tests, services, total_amount, payment_status, created_at) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        self.connection.commit()
        self.disconnect()
        return record

    def update(self, record: MedicalRecord):
        self.connect()
        self.cursor.execute("update medical_records set full_name=?, doctor_name=?, staff_name=?, department_name=?,session_type=?, description=?, medications=?, nursing_care=?,lab_tests=?, services=?, total_amount=?, payment_status=?, created_at=? where unit_no=?")
        self.connection.commit()
        self.disconnect()

    def delete(self, unit_no):
        self.connect()
        self.cursor.execute("delete from medical_records where unit_no=?", (unit_no))
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from medical_records ")
        record_list = [MedicalRecord(*medical_record) for medical_record in self.cursor.fetchall()]
        self.disconnect()
        return record_list

    def find_by_id(self, unit_no):
        self.connect()
        self.cursor.execute("select * from medical_records where unit_no=?", [unit_no])
        medical_record = self.cursor.fetchone()
        self.disconnect()
        if medical_record:
            return MedicalRecord(*medical_record)
        return None
