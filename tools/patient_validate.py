import re


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


def address(address):
    if not (type(address) == str and re.match(r"^[\w,\-]{3,100}$", address)):
        raise ValueError("Invalid address !!!")
    else:
        return address


def username(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z\s]*$", username)):
        raise ValueError("Invalid Username !!!")
    else:
        return username


def password(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z\s]*$", password)):
        raise ValueError("Invalid Password !!!")
    else:
        return password


def phone_number_validator(phone_number):
    if not (type(phone_number) == str and re.match(r"^(09|\+989)\d{9}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_number

def full_name_validate(full_name):
    if not (type(full_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", full_name)):
        raise ValueError("Invalid full name !!!")
    else:
        return full_name

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


def notes_text_validator(notes_text):
    if not (type(notes_text) == str and re.match(r"^[a-zA-Z\s\d\"\'!?.,:;]$", notes_text)):
        raise ValueError("Invalid notes text !!!")
    else:
        return notes_text

def height_validate(height):
    if not (type(height) == int and height > 0):
        raise ValueError("Invalid height!!!")
    else:
        return height

def weight_validate(weight):
    if not (type(weight) == int and weight > 0):
        raise ValueError("Invalid weight!!!")
    else:
        return weight

def date_of_admission_validate(date_of_admission):
    if not (type(date_of_admission) == str and re.match(r"^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}:\d{2}(:\d{2})$", date_of_admission)):
        raise ValueError("Invalid date of admission !!!")
    else:
        return date_of_admission

def attending_physician(attending_physician):
    if not (type(attending_physician) == str and re.match(r"^[a-zA-Z\s]{3,30}$", attending_physician)):
        raise ValueError("Invalid attending physician !!!")
    else:
        return attending_physician

def kind_of_ad_validate(kind_of_ad):
    if not (type(kind_of_ad) == str and re.match(r"^[a-zA-Z\s]{3,30}$", kind_of_ad)):
        raise ValueError("Invalid kind of ad !!!")
    else:
        return kind_of_ad

def room_validate(room):
    if not (type(room) == int and room > 0):
        raise ValueError("Invalid room!!!")
    else:
        return room

def bed_validate(bed):
    if not (type(bed) == int and bed > 0):
         raise ValueError("Invalid bed!!!")
    else:
        return bed

def ward_validate(ward):
    if not (type(ward) == str and re.match(r"^[a-zA-Z\s]{3,20}$", ward)):
        raise ValueError("Invalid ward !!!")
    else:
        return ward



