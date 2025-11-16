# repository/medical_record_repository.py
import sqlite3
import json
from model.medical_record import MedicalRecord
from typing import List, Optional

class MedicalRecordRepository:
    DB_PATH = "db/hospital.db"

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.DB_PATH)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, record: MedicalRecord) -> MedicalRecord:
        self.connect()
        data = record.to_tuple()
        self.cursor.execute('''
            INSERT OR REPLACE INTO medical_records (
                unit_no, full_name, doctor_name, staff_name, department_name,
                session_type, description, medications, nursing_care,
                lab_tests, services, total_amount, payment_status, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        self.connection.commit()
        self.disconnect()
        return record

    def update(self, record: MedicalRecord):
        self.connect()
        data = record.to_tuple()
        self.cursor.execute('''
            UPDATE medical_records SET
                full_name=?, doctor_name=?, staff_name=?, department_name=?,
                session_type=?, description=?, medications=?, nursing_care=?,
                lab_tests=?, services=?, total_amount=?, payment_status=?, created_at=?
            WHERE unit_no=?
        ''', data[1:] + (data[0],))
        self.connection.commit()
        self.disconnect()

    def delete(self, unit_no: int):
        self.connect()
        self.cursor.execute("DELETE FROM medical_records WHERE unit_no=?", (unit_no,))
        self.connection.commit()
        self.disconnect()

    def find_all(self) -> List[MedicalRecord]:
        self.connect()
        self.cursor.execute("SELECT * FROM medical_records")
        rows = self.cursor.fetchall()
        record_list = [
            MedicalRecord(
                unit_no=row[0], full_name=row[1], doctor_name=row[2], staff_name=row[3],
                department_name=row[4], session_type=row[5], description=row[6],
                medications=json.loads(row[7] or '[]'),
                nursing_care=json.loads(row[8] or '[]'),
                lab_tests=json.loads(row[9] or '[]'),
                services=json.loads(row[10] or '[]'),
                total_amount=row[11], payment_status=row[12], created_at=row[13]
            ) for row in rows
        ]
        self.disconnect()
        return record_list

    def find_by_unit_no(self, unit_no: int) -> Optional[MedicalRecord]:
        self.connect()
        self.cursor.execute("SELECT * FROM medical_records WHERE unit_no=?", (unit_no,))
        row = self.cursor.fetchone()
        self.disconnect()
        if row:
            return MedicalRecord(
                unit_no=row[0], full_name=row[1], doctor_name=row[2], staff_name=row[3],
                department_name=row[4], session_type=row[5], description=row[6],
                medications=json.loads(row[7] or '[]'),
                nursing_care=json.loads(row[8] or '[]'),
                lab_tests=json.loads(row[9] or '[]'),
                services=json.loads(row[10] or '[]'),
                total_amount=row[11], payment_status=row[12], created_at=row[13]
            )
        return None
