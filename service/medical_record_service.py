# service/medical_record_service.py
from repository.medical_record_repository import MedicalRecordRepository
from model.medical_record import MedicalRecord

class MedicalRecordService:
    medical_record_repository = MedicalRecordRepository()

    @classmethod
    def save(cls, record: MedicalRecord):
        return cls.medical_record_repository.save(record)

    @classmethod
    def find_by_unit_no(cls, unit_no: int):
        record = cls.medical_record_repository.find_by_unit_no(unit_no)
        if record:
            return record
        else:
            raise Exception("Medical Record Not Found !!!")
