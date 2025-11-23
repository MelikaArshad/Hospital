from tkinter import *
from PIL import ImageTk, Image
from model import MedicalRecord
from view.department_veiw import DepartmentView
from view.doctor_veiw import DoctorView
from view.patient_veiw import PatientView
from view.staff_veiw import StaffView


class DashboardView:
    def __init__(self):
    
        self.window = Tk()
        self.window.title("Hospital")
        self.window.geometry("400x300")
        self.window.config(background="white")

        Label(self.window, text="Hospital", font=("Arial", 16)).pack(pady=20)

        
        Button(self.window, text="Departments", width=20, command=self.department_view).pack(pady=5)
        Button(self.window, text="Doctors", width=20, command=self.doctor_view).pack(pady=5)
        Button(self.window, text="Patients", width=20, command=self.patient_view).pack(pady=5)
        Button(self.window, text="Staffs", width=20, command=self.staff_view).pack(pady=5)

        self.window.mainloop()


    def department_view(self):
        ui = DepartmentView()

    def doctor_view(self):
        ui = DoctorView()

    def patient_view(self):
        ui = PatientView()

    def staff_view(self):
        ui = StaffView()
