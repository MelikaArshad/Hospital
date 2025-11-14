from tools.patient_validate import *

class Patient:
    def __init__(self, unit_no, full_name, father_name, national_code, birth_date,phone_number, age, height, weight,
                 attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text):
        self.unit_no = unit_no
        self.full_name = full_name
        self.father_name = father_name
        self.national_code = national_code
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.age = age
        self.height = height
        self.weight = weight
        self.attending_physician = attending_physician
        self.kind_of_ad = kind_of_ad
        self.date_of_admission = date_of_admission
        self.ward = ward
        self.room = room
        self.bed = bed
        self.notes_text = notes_text

    def validate(self):
        full_name_validator(self.full_name)
        father_name_validator(self.father_name)
        national_code_validator(self.national_code)
        birth_date_validator(self.birth_date)
        age_validator(self.age)
        phone_number_validator(self.phone_number)
        height_validator(self.height)
        weight_validator(self.weight)
        attending_physician_validator(self.attending_physician)
        kind_of_ad_validator(self.kind_of_ad)
        date_of_admission_validator(self.date_of_admission)
        ward_validator(self.ward)
        room_validator(self.room)
        bed_validator(self.bed)
        notes_text_validator(self.notes_text)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.unit_no, self.full_name, self.father_name, self.national_code, self.birth_date,
                self.age,self.phone_number ,self.height, self.weight, self.attending_physician, self.kind_of_ad, self.date_of_admission,
                self.ward, self.room, self.bed, self.notes_text))
