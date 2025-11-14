import sqlite3
from model import Staff


class StaffRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./db/hospital_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, staff):
        self.connect()
        self.cursor.execute("insert into staffs (full_name, father_name, national_code, personal_id_no, degree, birth_date, age, phone_number,address, username, password, ward, role) values (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            [staff.full_name, staff.father_name, staff.national_code, staff.personal_id_no, staff.degree, staff.birth_date, staff.age, staff.phone_number,
                 staff.address, staff.username, staff.password, staff.ward, staff.role])
        staff.id = self.cursor.lastrowid
        self.connection.commit()
        return staff

    def update(self, staff):
        self.connect()
        self.cursor.execute("update staffs set full_name=?, father_name=?, national_code=?, personal_id_no=?, degree=?, birth_date=?, age=?, phone_number=?,address=?, username=?, password=?, ward=?, role=?  where staff_id=?",
                            [staff.staff_id,staff.full_name, staff.father_name, staff.national_code, staff.personal_id_no, staff.degree, staff.birth_date, staff.age, staff.phone_number,
                 staff.address, staff.username, staff.password, staff.ward, staff.role])
        self.connection.commit()
        self.disconnect()
        return staff

    def delete(self, staff_id):
        self.connect()
        self.cursor.execute("delete from staffs where staff_id=?",
                            [staff_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from staffs")
        staff_list = [Staff(*staff) for staff in self.cursor.fetchall()]
        self.disconnect()
        return staff_list

    def find_by_id(self, staff_id):
        self.connect()
        self.cursor.execute("select * from staffs where staff_id=?", [staff_id])
        staff = self.cursor.fetchone()
        self.disconnect()
        if staff:
            return Staff(*staff)
        return None

    def find_by_name(self, full_name):
        self.connect()
        self.cursor.execute("select * from staffs where full_name like ?", [full_name + "%"])
        staff_list = [Staff(*staff) for staff in self.cursor.fetchall()]
        self.disconnect()
        return staff_list

    def find_by_national_code(self, national_code):
        self.connect()
        self.cursor.execute("select * from staffs where national_code like ?", [national_code + "%"])
        staff_list = [Staff(*staff) for staff in self.cursor.fetchall()]
        self.disconnect()
        return staff_list


    def find_by_personal_id_no(self, personal_id_no):
        self.connect()
        self.cursor.execute("select * from staffs where personal_id_no like ?", [personal_id_no + "%"])
        staff_list = [Staff(*staff) for staff in self.cursor.fetchall()]
        self.disconnect()
        return staff_list
