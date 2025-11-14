from repository import PatientRepository


class PatientService:
    patient_repository = PatientRepository()

    @classmethod
    def save(cls, patient):
        return cls.patient_repository.save(patient)

    @classmethod
    def update(cls,patient ):
        patient_result = cls.patient_repository.find_by_unit_no(patient.unit_no)
        if patient_result:
            return cls.patient_repository.update(patient)
        else:
            raise Exception("patient Not Found !!!")

    @classmethod
    def delete(cls, unit_no):
        patient = cls.patient_repository.find_by_unit_no(unit_no)
        if patient:
            cls.patient_repository.delete(unit_no)
            return patient
        else:
            raise Exception("patient Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.patient_repository.find_all()

    @classmethod
    def find_by_unit_no(cls, unit_no):
        patient = cls.patient_repository.find_by_unit_no(unit_no)
        if patient:
            return patient
        else:
            raise Exception("patient Not Found !!!")

    @classmethod
    def find_by_name(cls, full_name):
        return cls.patient_repository.find_by_name(full_name)

    @classmethod
    def find_by_national_code(cls, national_code):
        return cls.patient_repository.find_by_national_code(national_code)

