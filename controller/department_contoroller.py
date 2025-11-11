from model import Department
from service import DepartmentService
from tools import Logger


class DepartmentController:
    department_service = DepartmentService()

    @classmethod
    def save(cls,department_name,department_controller):
        try:
            department = Department(None,department_name,department_controller)
            department.validate()
            department= cls.department_service.save(department)
            Logger.info(f"department {department} saved")
            return True, f"department Saved Successfully"
        except Exception as e:
            Logger.error(f"department Saved Error: {e}")
            return False, e

    @classmethod
    def update(cls, department_id,department_name,department_controller):
        try:
            department = Department(department_id,department_name,department_controller)
            department.validate()
            department = cls.department_service.update(department)
            Logger.info(f"department {department} updated")
            return True, "department Updated Successfully"
        except Exception as e:
            Logger.error(f"department Updated Error: {e}")
            return False, e

    @classmethod
    def delete(cls, department_id):
        try:
            department = cls.department_service.delete(department_id)
            Logger.info(f"department {department} deleted")
            return True, f"department Deleted Successfully"
        except Exception as e:
            Logger.error(f"department Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            department_list = cls.department_service.find_all()
            Logger.info("department FindAll")
            return True, department_list
        except Exception as e:
            Logger.error(f"department FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, department_id):
        try:
            department = cls.department_service.find_by_id(department_id)
            Logger.info(f"department FindById {department_id}")
            return True, department
        except Exception as e:
            Logger.error(f"{e} With Id {department_id}")
            return False, e

    @classmethod
    def find_by_name(cls, full_name):
        try:
            department_list = cls.department_service.find_by_name(full_name)
            Logger.info(f"department FindByName {full_name}")
            return True, department_list
        except Exception as e:
            Logger.error(f"department FindByName Error: {e}")
            return False, e

