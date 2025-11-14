from repository import StaffRepository


class StaffService:
    staff_repository = StaffRepository()

    @classmethod
    def save(cls, staff):
        return cls.staff_repository.save(staff)

    @classmethod
    def update(cls, staff):
        staff_result = cls.staff_repository.find_by_id(staff.staff_id)
        if staff_result:
            return cls.staff_repository.update(staff)
        else:
            raise Exception("staff Not Found !!!")

    @classmethod
    def delete(cls, staff_id):
        staff = cls.staff_repository.find_by_id(staff_id)
        if staff:
            cls.staff_repository.delete(staff_id)
            return staff
        else:
            raise Exception("staff Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.staff_repository.find_all()

    @classmethod
    def find_by_id(cls, staff_id):
        staff = cls.staff_repository.find_by_id(staff_id)
        if staff:
            return staff
        else:
            raise Exception("staff Not Found !!!")

    @classmethod
    def find_by_name(cls, full_name):
        return cls.staff_repository.find_by_name(full_name)

    @classmethod
    def find_by_national_code(cls, national_code):
        return cls.staff_repository.find_by_national_code(national_code)

    @classmethod
    def find_by_personal_id_no(cls, personal_id_no):
        return cls.staff_repository.find_by_personal_id_no(personal_id_no)