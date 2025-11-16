from datetime import datetime
from model import Patient,Doctor,Staff,Department
# from tools.medical_record import MedicalRecordValidator

class MedicalRecord(Patient):
    def __init__(self,record_id,unit_no,full_name,doctor_name,staff_name,department_name,session_type,description,medication,nursing_care,lab_tests,services,total_amount,payment_status,date_of_admission):
        super().__init__(unit_no,full_name,date_of_admission)
        self.record_id =record_id
        self.doctor_name = doctor_name
        self.staff_name = staff_name
        self.department_name = department_name
        self.session_type = session_type
        self.description = description
        self.medication = medication
        self.nursing_care = nursing_care
        self.lab_tests = lab_tests
        self.services = services
        self.total_amount = total_amount
        self.payment_status = payment_status


    def validate(self):
        pass

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.record_id,self.unit_no,self.full_name,self.doctor_name,self.staff_name,self.department_name,self.session_type,self.description,self.medication,self.nursing_care,self.lab_tests,self.services,self.total_amount,self.payment_status,self.date_of_admission))
