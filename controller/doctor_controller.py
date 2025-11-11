from model import Doctor
from service import DoctorService
from tools import Logger


class DoctorController:
    doctor_service = DoctorService()

    @classmethod
    def save(cls, full_name ,department_controller,father_name, national_code, personal_id_no, degree, birth_date, age,
                 phone_number,address, username, password):
        try:
            doctor = Doctor(None,full_name ,department_controller,father_name, national_code, personal_id_no, degree, birth_date, age,
                 phone_number,address, username, password)
            doctor.validate()
            doctor = cls.doctor_service.save(doctor)
            Logger.info(f"doctor {doctor} saved")
            return True, f"doctor Saved Successfully"
        except Exception as e:
            Logger.error(f"doctor Saved Error: {e}")
            return False, e

    @classmethod
    def update(cls, doctor_id,full_name ,department_controller,father_name, national_code, personal_id_no, degree, birth_date, age,
                 phone_number,address, username, password):
        try:
            doctor =Doctor(doctor_id,full_name ,department_controller,father_name, national_code, personal_id_no, degree, birth_date, age,
                 phone_number,address, username, password)
            doctor.validate()
            doctor = cls.doctor_service.update(doctor)
            Logger.info(f"doctor {doctor} updated")
            return True, "doctor Updated Successfully"
        except Exception as e:
            Logger.error(f"doctor Updated Error: {e}")
            return False, e

    @classmethod
    def delete(cls, doctor_id):
        try:
            doctor = cls.doctor_service.delete(doctor_id)
            Logger.info(f"doctor {doctor} deleted")
            return True, f"doctor Deleted Successfully"
        except Exception as e:
            Logger.error(f"doctor Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            doctor_list = cls.doctor_service.find_all()
            Logger.info("doctor FindAll")
            return True, doctor_list
        except Exception as e:
            Logger.error(f"doctor FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, doctor_id):
        try:
            doctor = cls.doctor_service.find_by_id(doctor_id)
            Logger.info(f"doctor FindById {doctor_id}")
            return True, doctor
        except Exception as e:
            Logger.error(f"{e} With Id {doctor_id}")
            return False, e

    @classmethod
    def find_by_name(cls, full_name):
        try:
            doctor_list = cls.doctor_service.find_by_name(full_name)
            Logger.info(f"doctor FindByName {full_name}")
            return True, doctor_list
        except Exception as e:
            Logger.error(f"doctor FindByName Error: {e}")
            return False, e

    @classmethod
    def find_by_national_code(cls, national_code):
        try:
            bank_list = cls.national_code.find_by_national_code(national_code)
            Logger.info(f"Staff Find By national code {national_code}")
            return True, bank_list
        except Exception as e:
            Logger.error(f"Staff Find By national code Error: {e}")
            return False, e
