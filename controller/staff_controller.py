from model import Staff
from service import StaffService
from tools import Logger


class StaffController:
    staff_service = StaffService()

    @classmethod
    def save(cls, full_name, family_name, father_name, national_code, personal_id_no, degree, birth_date, age,
             address, phone_number, username, password, ward, role):
        try:
            staff = Staff(None, full_name, family_name, father_name, national_code, personal_id_no, degree, birth_date,
                          age,
                          address, phone_number, username, password, ward, role)
            staff.validate()
            staff = cls.staff_service.save(staff)
            Logger.info(f"Staff {staff} saved")
            return True, f"Staff Saved Successfully"
        except Exception as e:
            Logger.error(f"Staff Saved Error: {e}")
            return False, e

    @classmethod
    def update(cls, staff_id, full_name, family_name, father_name, national_code, personal_id_no, degree, birth_date,
               age,
               address, phone_number, username, password, ward, role):
        try:
            staff = Staff(staff_id, full_name, family_name, father_name, national_code, personal_id_no, degree,
                          birth_date,
                          age, phone_number,
                          address, username, password, ward, role)
            staff.validate()
            staff = cls.staff_service.update(staff)
            Logger.info(f"Staff {staff} updated")
            return True, "Staff Updated Successfully"
        except Exception as e:
            Logger.error(f"Staff Updated Error: {e}")
            return False, e

    @classmethod
    def delete(cls, staff_id):
        try:
            staff = cls.staff_service.delete(staff_id)
            Logger.info(f"Staff {staff} deleted")
            return True, f"Staff Deleted Successfully"
        except Exception as e:
            Logger.error(f"Staff Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            staff_list = cls.staff_service.find_all()
            Logger.info("Staff FindAll")
            return True, staff_list
        except Exception as e:
            Logger.error(f"Staff FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, staff_id):
        try:
            staff = cls.staff_service.find_by_id(staff_id)
            Logger.info(f"Staff FindById {staff_id}")
            return True, staff
        except Exception as e:
            Logger.error(f"{e} With Id {staff_id}")
            return False, e

    @classmethod
    def find_by_name(cls, full_name):
        try:
            staff_list = cls.staff_service.find_by_name(full_name)
            Logger.info(f"Staff FindByName {full_name}")
            return True, staff_list
        except Exception as e:
            Logger.error(f"Staff FindByName Error: {e}")
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
