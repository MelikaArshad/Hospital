from tools.doctor_validate import *

class Doctor:
    def __init__(self,doctor_id,full_name ,department_controller,father_name, national_code, personal_id_no, degree, birth_date, age,
                 phone_number,address, username, password):
        self.doctor_id = doctor_id
        self.full_name = full_name
        self.department_controller = department_controller
        self.father_name = father_name
        self.national_code = national_code
        self.personal_id_no = personal_id_no
        self.degree = degree
        self.birth_date = birth_date
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.username = username
        self.password = password

    def validate(self):
        full_name_validate(self.full_name)
        department_controller_validate(self.department_controller)
        father_name_validate(self.father_name)
        national_code_validate(self.national_code)
        personal_id_no_validate(self.personal_id_no)
        degree_validate(self.degree)
        birth_date_validate(self.birth_date)
        age_validate(self.age)
        address_validate(self.address)
        phone_number_validate(self.phone_number)
        username_validate(self.username)
        password_validate(self.password)

    def __repr__(self):
            return f"{self.__dict__}"

    def to_tuple(self):
            return tuple((self.doctor_id ,self.full_name ,self.department_controller ,self.father_name ,self.national_code ,self.personal_id_no ,self.degree,self.birth_date ,self.age ,self.address ,self.phone_number,self.username ,self.password))
