# view/medical_record_window.py
import tkinter as tk
from controller.doctor_controller import DoctorController
from controller.staff_controller import StaffController
from controller.department_controller import DepartmentController

class MedicalRecordWindow:
    def __init__(self, patient, data):
        self.win = tk.Toplevel()
        self.win.title(f"Medical Record - {patient.full_name}")
        self.win.geometry("900x600")
        self.win.configure(bg="#f8f9fa")

        # --- اطلاعات اصلی ---
        info_frame = tk.Frame(self.win, bg="#f8f9fa")
        info_frame.pack(fill="x", padx=20, pady=10)

        doctor = DoctorController.find_by_id(data["doctor_id"])[1] if data["doctor_id"] else None
        staff = StaffController.find_by_id(data["staff_id"])[1] if data["staff_id"] else None
        dept = DepartmentController.find_by_id(data["department_id"])[1] if data["department_id"] else None

        lines = [
            f"Patient: {patient.full_name} | Unit No: {patient.unit_no}",
            f"National ID: {patient.national_code} | Age: {patient.age}",
            f"Doctor: {doctor.full_name if doctor else '—'}",
            f"Nurse: {staff.full_name if staff else '—'}",
            f"Department: {dept.department_name if dept else '—'}",
            f"Record Type: {data['record_type']} | Date: {data['created_at']}",
            f"Total: {data['total_amount']:,} | Status: {data['payment_status']}"
        ]

        for text in lines:
            tk.Label(info_frame, text=text, font=("Arial", 11), anchor="w", bg="#f8f9fa").pack(fill="x", pady=2)

        # --- داروها ---
        if data["medications"]:
            med_frame = tk.LabelFrame(self.win, text="Medications", font=("Arial", 11, "bold"))
            med_frame.pack(fill="x", padx=20, pady=10)
            for m in data["medications"]:
                tk.Label(med_frame, text=f"• {m['name']} — {m.get('dosage','')} — {m.get('frequency','')}", anchor="w").pack(fill="x", padx=10)

        # --- مراقبت ---
        if data["nursing_care"]:
            care_frame = tk.LabelFrame(self.win, text="Nursing Care", font=("Arial", 11, "bold"))
            care_frame.pack(fill="x", padx=20, pady=10)
            for c in data["nursing_care"]:
                tk.Label(care_frame, text=f"• {c['type']} — {c.get('description','')}", anchor="w").pack(fill="x", padx=10)
