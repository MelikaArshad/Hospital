import re


def department_name_validate(department_name):
    if not (type(department_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", department_name)):
        raise ValueError("Invalid department name !!!")
    else:
        return department_name


def department_controller_validate(department_controller):
    if not (type(department_controller) == str and re.match(r"^[a-zA-Z\s]{3,30}$", department_controller)):
        raise ValueError("Invalid department controller !!!")
    else:
        return department_controller
