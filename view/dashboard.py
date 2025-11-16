from tkinter import *
from PIL import ImageTk, Image
from model import MedicalRecord
from view import *


class DashboardView:
    def department_view(self):
        ui = DepartmentView()

    def doctor_view(self):
        ui = DoctorView()

    def patient_view(self):
        ui = PatientView()

    def staff_view(self):
        ui = StaffView()
