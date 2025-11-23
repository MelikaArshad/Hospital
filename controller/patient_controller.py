from model import Patient
from service.patient_service import PatientService
from tools import Logger


class PatientController:
    patient_service = PatientService()

    @classmethod
    def save(cls,unit_no, full_name, father_name, national_code, birth_date, phone_number, age, height, weight,
             attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text):
        try:
            patient = Patient(unit_no, full_name, father_name, national_code, birth_date, phone_number, age, height,
                              weight,
                              attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text)
            patient.validate()
            patient = cls.patient_service.save(patient)
            Logger.info(f"Patient {patient} saved")
            return True, f"Patient Saved Successfully"
        except Exception as e:
            Logger.error(f"Patient Saved Error: {e}")
            return False, e

    @classmethod
    def update(cls, unit_no, full_name, father_name, national_code, birth_date, phone_number, age, height, weight,
               attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text):
        try:
            patient = Patient(unit_no, full_name, father_name, national_code, birth_date, phone_number, age, height,
                              weight,
                              attending_physician, kind_of_ad, date_of_admission, ward, room, bed, notes_text)
            patient.validate()
            patient = cls.patient_service.update(patient)
            Logger.info(f"Patient {patient} updated")
            return True, "Patient Updated Successfully"
        except Exception as e:
            Logger.error(f"Patient Updated Error: {e}")
            return False, e

    @classmethod
    def delete(cls, unit_no):
        try:
            patient = cls.patient_service.delete(unit_no)
            Logger.info(f"Patient {patient} deleted")
            return True, f"Patient Deleted Successfully"
        except Exception as e:
            Logger.error(f"Patient Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            patient_list = cls.patient_service.find_all()
            Logger.info("patient FindAll")
            return True, patient_list
        except Exception as e:
            Logger.error(f"patient FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_unit_no(cls, unit_no):
        try:
            patient = cls.patient_service.find_by_unit_no(unit_no)
            Logger.info(f"Patient Find By unit_no {unit_no}")
            return True, patient
        except Exception as e:
            Logger.error(f"{e} With unit_no {unit_no}")
            return False, e

    @classmethod
    def find_by_name(cls, full_name):
        try:
            patient_list = cls.patient_service.find_by_name(full_name)
            Logger.info(f"Patient FindByName {full_name}")
            return True, patient_list
        except Exception as e:
            Logger.error(f"Patient FindByName Error: {e}")
            return False, e

    @classmethod
    def find_by_national_code(cls, national_code):
        try:
            patient_list = cls.patient_service.find_by_national_code(national_code)
            Logger.info(f"Bank FindBy national code {national_code}")
            return True, patient_list
        except Exception as e:
            Logger.error(f"Bank FindBy national code Error: {e}")
            return False, e
