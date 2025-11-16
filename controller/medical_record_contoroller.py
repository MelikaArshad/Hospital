# controller/medical_record_controller.py
from service.medical_record_service import MedicalRecordService
from tools.logger import Logger

class MedicalRecordController:
    @classmethod
    def save(cls, unit_no, full_name, doctor_name, staff_name, department_name,
             session_type, description="", medications=None, nursing_care=None,
             lab_tests=None, services=None, total_amount=0.0, payment_status="Pending"):
        from model.medical_record import MedicalRecord
        record = MedicalRecord(
            unit_no=unit_no, full_name=full_name, doctor_name=doctor_name,
            staff_name=staff_name, department_name=department_name,
            session_type=session_type, description=description,
            medications=medications or [], nursing_care=nursing_care or [],
            lab_tests=lab_tests or [], services=services or [],
            total_amount=total_amount, payment_status=payment_status
        )
        return MedicalRecordService.save(record)

    @classmethod
    def find_by_unit_no(cls, unit_no: int):
        try:
            status, record = MedicalRecordService.find_by_unit_no(unit_no)
            if status:
                Logger.info(f"MedicalRecord FindByUnitNo (unit_no={unit_no})")
                return True, record
            else:
                Logger.info(f"MedicalRecord Not Found (unit_no={unit_no})")
                return False, "Record Not Found"
        except Exception as e:
            Logger.error(f"MedicalRecord FindByUnitNo Error: {e}")
            return False, f"Error: {e}"
