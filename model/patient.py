class Patient:
    def __init__(self, unit_no, name, family_name, father_name, national_code, birth_date, age, height, weight,
                 attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text):
        self.unit_no = unit_no
        self.name = name
        self.family_name = family_name
        self.father_name = father_name
        self.national_code = national_code
        self.birth_date = birth_date
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
        pass

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self.unit_no, self.name, self.family_name, self.father_name, self.national_code, self.birth_date,
                self.age, self.height, self.weight, self.attending_physician, self.kind_of_ad, self.date_of_admission,
                self.ward, self.room, self.bed, self.notes_text)
