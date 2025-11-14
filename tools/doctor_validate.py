import re


def full_name_validate(full_name):
    if not (type(full_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", full_name)):
        raise ValueError("Invalid full_name !!!")
    else:
        return full_name


def department_controller_validate(department_controller):
    if not (type(department_controller) == str and re.match(r"^[a-zA-Z\s]{3,30}$", department_controller)):
        raise ValueError("Invalid department_controller !!!")
    else:
        return department_controller


def father_name_validate(father_name):
    if not (type(father_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", father_name)):
        raise ValueError("Invalid father_name !!!")
    else:
        return father_name


def national_code_validate(national_code):
    if not (type(national_code) == int and national_code > 0):
        raise ValueError("Invalid national_code !!!")
    else:
        return national_code


def personal_id_no_validate(personal_id_no):
    if not (type(personal_id_no) == int and personal_id_no > 0):
        raise ValueError("Invalid Personal Id No!!!")
    else:
        return personal_id_no


def degree_validate(degree):
    if not (type(degree) == str and re.match(r"^[a-zA-Z\s]{3,40}$", degree)):
        raise ValueError("Invalid degree !!!")
    else:
        return degree


def birth_date_validate(birth_date):
    if not (type(birth_date) == str and re.match(r"^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}:\d{2}(:\d{2})$", birth_date)):
        raise ValueError("Invalid birth date !!!")
    else:
        return birth_date


def age_validate(age):
    if not 0 <= age <= 100:
        raise ValueError("Invalid age !!!")
    else:
        return age


def address_validate(address):
    if not (type(address) == str and re.match(r"^[\w,\-]{3,100}$", address)):
        raise ValueError("Invalid address !!!")
    else:
        return address


def username_validate(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z\s]*$", username)):
        raise ValueError("Invalid Username !!!")
    else:
        return username


def password_validate(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z\s]*$", password)):
        raise ValueError("Invalid Password !!!")
    else:
        return password


def phone_number_validate(phone_number):
    if not (type(phone_number) == str and re.match(r"^(09|\+989)\d{9}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_number


