import sqlite3
from model import Department


class DepartmentRepository:
    def __init__(self):
        self.cursor = None
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("./db/hospital_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, department):
        self.connect()
        self.cursor.execute("insert into banks (department_name,department_controller) values (?,?)",
                            [department.department_name,department.department_controller])
        department.id = self.cursor.lastrowid
        self.connection.commit()
        return department

    def update(self, department):
        self.connect()
        self.cursor.execute("update banks set department_name=?,department_controller=? where department_id=?",
                            [department.department_id,department.department_name,department.department_controller])
        self.connection.commit()
        self.disconnect()
        return department

    def delete(self, department_id):
        self.connect()
        self.cursor.execute("delete from departments where department_id=?",
                            [department_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from departments")
        department_list = [Department(*department) for department in self.cursor.fetchall()]
        self.disconnect()
        return department_list

    def find_by_id(self, department_id):
        self.connect()
        self.cursor.execute("select * from departments where department_id=?", [department_id])
        bank = self.cursor.fetchone()
        self.disconnect()
        if department:
            return Department(*department)
        return None

    def find_by_name(self, department_name):
        self.connect()
        self.cursor.execute("select * from departments where department_name like ?", [department_name + "%"])
        department_list = [Department(*department) for department in self.cursor.fetchall()]
        self.disconnect()
        return department_list

