from repository import DepartmentRepository


class DepartmentService:
    department_repository = DepartmentRepository()

    @classmethod
    def save(cls, department):
        return cls.department_repository.save(department)

    @classmethod
    def update(cls,department ):
        department_result = cls.department_repository.find_by_id(department.department_id)
        if department_result:
            return cls.department_repository.update(department)
        else:
            raise Exception("department Not Found !!!")

    @classmethod
    def delete(cls, department_id):
        department = cls.department_repository.find_by_id(department_id)
        if department:
            cls.department_repository.delete(department_id)
            return department
        else:
            raise Exception("department Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.department_repository.find_all()

    @classmethod
    def find_by_id(cls, department_id):
        department = cls.department_repository.find_by_id(department_id)
        if department:
            return department
        else:
            raise Exception("department Not Found !!!")

    @classmethod
    def find_by_name(cls, full_name):
        return cls.department_repository.find_by_name(full_name)

