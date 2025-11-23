import sqlite3
from model import Doctor
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "db/hospital.db")

class DoctorRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, doctor):
        self.connect()
        self.cursor.execute("insert into doctors (full_name ,department_controller,father_name, national_code, personal_id_no, degree, birth_date, age,phone_number, address, username, password) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
         [doctor.full_name, doctor.department_controller, doctor.father_name, doctor.national_code,
          doctor.personal_id_no, doctor.degree, doctor.birth_date, doctor.age,
          doctor.phone_number, doctor.address, doctor.username, doctor.password])
        doctor.id = self.cursor.lastrowid
        self.connection.commit()
        return doctor

    def update(self, doctor ):
        self.connect()
        self.cursor.execute("update doctors set full_name=? ,department_controller=?,father_name=?, national_code=?, personal_id_no=?, degree=?, birth_date=?, age=?,phone_number =?, address =?, username =?, password =? where doctor_id =?",
        [doctor.doctor_id, doctor.full_name, doctor.department_controller, doctor.father_name, doctor.national_code, doctor.personal_id_no, doctor.degree, doctor.birth_date, doctor.age,doctor.phone_number, doctor.address, doctor.username, doctor.password])
        self.connection.commit()
        self.disconnect()
        return doctor

    def delete(self, doctor_id):
        self.connect()
        self.cursor.execute("delete from doctors where doctor_id=?",
                            [doctor_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from doctors")
        doctor_list = [Doctor(*doctor) for doctor  in self.cursor.fetchall()]
        self.disconnect()
        return doctor_list

    def find_by_id(self, doctor_id):
        self.connect()
        self.cursor.execute("select * from doctors where doctor_id=?", [doctor_id])
        doctor= self.cursor.fetchone()
        self.disconnect()
        if doctor:
            return Doctor(*doctor)
        return None

    def find_by_name(self, full_name):
        self.connect()
        self.cursor.execute("select * from doctors where full_name like ?", [full_name + "%"])
        doctor_list = [Doctor(*doctor) for doctor in self.cursor.fetchall()]
        self.disconnect()
        return doctor_list

    def find_by_national_code(self, national_code):
        self.connect()
        self.cursor.execute("select * from doctors where national_code like ?", [national_code + "%"])
        doctor_list = [Doctor(*doctor) for doctor in self.cursor.fetchall()]
        self.disconnect()
        return doctor_list


    def find_by_personal_id_no(self, personal_id_no):
        self.connect()
        self.cursor.execute("select * from doctors where personal_id_no like ?", [personal_id_no + "%"])
        doctor_list = [Doctor(*doctor) for doctor in self.cursor.fetchall()]
        self.disconnect()
        return doctor_list
