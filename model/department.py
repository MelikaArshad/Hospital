from tools.department_validate import *

class Department:
    def __init__(self,department_id,department_name,department_controller):
        self.department_id = department_id
        self.department_name = department_name
        self.department_controller = department_controller

    def validate(self):
        department_name_validate(self.department_name)
        department_controller_validate(self.department_controller)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.department_id,self.department_name,self.department_controller))
