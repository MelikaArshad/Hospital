from repository import DoctorRepository


class DoctorService:
    doctor_repository = DoctorRepository()

    @classmethod
    def save(cls, doctor):
        return cls.doctor_repository.save(doctor)

    @classmethod
    def update(cls,doctor ):
        doctor_result = cls.doctor_repository.find_by_id(doctor.doctor_id)
        if doctor_result:
            return cls.doctor_repository.update(doctor)
        else:
            raise Exception("doctor Not Found !!!")

    @classmethod
    def delete(cls, doctor_id):
        doctor = cls.doctor_repository.find_by_id(doctor_id)
        if doctor:
            cls.doctor_repository.delete(doctor_id)
            return doctor
        else:
            raise Exception("doctor Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.doctor_repository.find_all()

    @classmethod
    def find_by_id(cls, doctor_id):
        doctor = cls.doctor_repository.find_by_id(doctor_id)
        if doctor:
            return doctor
        else:
            raise Exception("doctor Not Found !!!")

    @classmethod
    def find_by_name(cls, full_name):
        return cls.doctor_repository.find_by_name(full_name)

    @classmethod
    def find_by_national_code(cls, national_code):
        return cls.doctor_repository.find_by_national_code(national_code)

    @classmethod
    def find_by_personal_id_no(cls, personal_id_no):
        return cls.doctor_repository.find_by_personal_id_no(personal_id_no)