from tools.staff_validate import *
class Staff:
    def __init__(self, staff_id, full_name, father_name, national_code, personal_id_no, degree, birth_date, age, phone_number,
                 address, username, password, ward, role):
       self.staff_id = staff_id
       self.full_name = full_name
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
       self.ward = ward
       self.role = role

    def validate(self):
        full_name_validate(self.full_name)
        father_name_validate(self.father_name)
        national_code_validate(self.national_code)
        personal_id_no_validate(self.personal_id_no)
        degree_validate(self.degree)
        birth_date_validate(self.birth_date)
        age_validate(self.age)
        phone_number_validate(self.phone_number)
        address_validate(self.address)
        username_validate(self.username)
        password_validate(self.password)
        ward_validate(self.ward)
        role_validate(self.role)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.staff_id,self.full_name,self.father_name,self.national_code,self.personal_id_no,self.degree,self.birth_date,self.age,self.phone_number,self.address,self.username,self.password,self.ward,self.role))