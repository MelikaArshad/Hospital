from service.medical_record_service import MedicalRecordService
from model.medical_record import MedicalRecord
from tools import Logger

class MedicalRecordController:
    medical_record_service=MedicalRecordService()
    @classmethod
    def save(cls, unit_no, full_name, doctor_name, staff_name, department_name,
             session_type, description, medications, nursing_care,
             lab_tests, services, total_amount, payment_status):
        try:
            medical_record = MedicalRecord(None,unit_no, full_name, doctor_name, staff_name, department_name,
             session_type, description, medications, nursing_care,
             lab_tests, services, total_amount, payment_status)
            medical_record.validate()
            medical_record= cls.medical_record_service.save(medical_record)
            Logger.info(f"medical_record {medical_record} saved")
            return True, f"medical_record Saved Successfully"
        except Exception as e:
            Logger.error(f"medical_record Saved Error: {e}")
            return False, e



    @classmethod
    def find_by_unit_no(cls, unit_no):
        try:
            status, record = MedicalRecordService.find_by_unit_no(unit_no)
            if status:
                Logger.info(f"MedicalRecord FindByUnitNo {unit_no}")
                return True, record
            else:
                Logger.info(f"MedicalRecord Not Found {unit_no}")
                return False, "Record Not Found"
        except Exception as e:
            Logger.error(f"MedicalRecord FindByUnitNo Error: {e}")
            return False, e
