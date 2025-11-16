from view import *
from model import Patient
from controller.patient_controller import PatientController


class PatientView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1300x750")
        self.window.title("Patient Management")

        self.unit_no = LabelWithEntry(self.window, "Unit No", 20, 20, data_type=IntVar, state="readonly")
        self.full_name = LabelWithEntry(self.window, "Full Name", 20, 60)
        self.father_name = LabelWithEntry(self.window, "Father Name", 20, 100)
        self.national_code = LabelWithEntry(self.window, "National Code", 20, 140, data_type=IntVar)
        self.birth_date = LabelWithEntry(self.window, "Birth Date", 20, 180)
        self.phone_number = LabelWithEntry(self.window, "Phone Number", 20, 220)
        self.age = LabelWithEntry(self.window, "Age", 20, 260, data_type=IntVar)
        self.height = LabelWithEntry(self.window, "Height", 20, 300, data_type=IntVar)
        self.weight = LabelWithEntry(self.window, "Weight", 20, 340, data_type=IntVar)
        self.attending_physician = LabelWithEntry(self.window, "Attending Physician", 20, 380)
        self.kind_of_ad = LabelWithEntry(self.window, "Kind Of Ad", 20, 420)
        self.date_of_admission = LabelWithEntry(self.window, "Date Of Admission", 20, 460)
        self.ward = LabelWithEntry(self.window, "Ward", 20, 500)
        self.room = LabelWithEntry(self.window, "Room", 20, 540, data_type=IntVar)
        self.bed = LabelWithEntry(self.window, "Bed", 20, 580, data_type=IntVar)
        self.notes_text = LabelWithEntry(self.window, "Notes Text", 20, 620)

        self.table = Table(
            self.window,
            ["Unit NO", "Full Name", "Father Name", "National Code","Birth Name","Phone Number","Age","Height","Weight","Attending Physician","Kind Of Ad","Date Of Admission","Ward","Room","Bed", "Notes Text" ],
            [80, 100, 90, 100, 50, 50, 50, 110, 90,70,60,60],
            520, 20,
            30,
            self.select_from_table
        )

        Button(self.window, text="Select Patient", width=15, command=self.select_patient).place(x=20, y=680)
        Button(self.window, text="Refresh", width=12, command=self.refresh).place(x=180, y=680)
        Button(self.window, text="Save", width=12, command=self.save_click).place(x=300, y=680)
        Button(self.window, text="Edit", width=12, command=self.edit_click).place(x=420, y=680)
        Button(self.window, text="Delete", width=12, command=self.delete_click).place(x=540, y=680)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = PatientController.save(
        self.unit_no.get(),
        self.full_name.get(),
        self.father_name.get(),
        self.national_code.get(),
        self.birth_date.get(),
        self.phone_number.get(),
        self.age.get(),
        self.height.get(),
        self.weight.get(),
        self.attending_physician.get(),
        self.kind_of_ad.get(),
        self.date_of_admission.get(),
        self.ward.get(),
        self.room.get(),
        self.bed.get(),
        self.notes_text.get())

        if status:
            messagebox.showinfo("Patient Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Patient Save Error", message)

    def edit_click(self):
        status, message = PatientController.update( self.unit_no.get(),
        self.full_name.get(),
        self.father_name.get(),
        self.national_code.get(),
        self.birth_date.get(),
        self.phone_number.get(),
        self.age.get(),
        self.height.get(),
        self.weight.get(),
        self.attending_physician.get(),
        self.kind_of_ad.get(),
        self.date_of_admission.get(),
        self.ward.get(),
        self.room.get(),
        self.bed.get(),
        self.notes_text.get())
        if status:
            messagebox.showinfo("Patient Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Patient Update Error", message)

    def delete_click(self):
        status, message = PatientController.delete(self.unit_no.get())
        if status:
            messagebox.showinfo("Patient Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Patient Delete Error", message)
    def view_record_click(self):
        if not self.selected_patient:
            messagebox.showwarning(title="Warning", message="Select a patient")
            return
        repo = MedicalRecordRepository()
        data = repo.find_by_patient(self.selected_patient)
        if data:
            status, patient = PatientController.find_by_id(self.selected_patient)
            if status:
                MedicalRecordWindow(patient, data)
        else:
            messagebox.showinfo(title="No Record", message="No medical record found")

    def reset_form(self):
        self.unit_no.clear()
        self.full_name.clear()
        self.father_name.clear()
        self.national_code.clear()
        self.birth_date.clear()
        self.phone_number.clear()
        self.age.clear()
        self.height.clear()
        self.weight.clear()
        self.attending_physician.clear()
        self.kind_of_ad.clear()
        self.date_of_admission.clear()
        self.ward.clear()
        self.room.clear()
        self.bed.clear()
        self.notes_text.clear()

        status, patient_list = PatientController.find_all()
        self.table.refresh_table(patient_list)

    def select_from_table(self, selected_patient):
        if selected_patient:
            status, patient = PatientController.find_by_unit_no(selected_patient[0])
            if status:
                patient = Patient(*selected_patient)
                self.unit_no.set(patient.unit_no)
                self.full_name.set(patient.full_name)
                self.father_name.set(patient.father_name)
                self.national_code.set(patient.national_code)
                self.birth_date.set(patient.birth_date)
                self.phone_number.set(patient.phone_number)
                self.age.set(patient.age)
                self.height.set(patient.height)
                self.weight.set(patient.weight)
                self.attending_physician.set(patient.attending_physician)
                self.kind_of_ad.set(patient.kind_of_ad)
                self.date_of_admission.set(patient.date_of_admission)
                self.ward.set(patient.ward)
                self.room.set(patient.room)
                self.bed.set(patient.bed)
                self.notes_text.set(patient.notes_text)

    def select_patient(self):
        if self.unit_no.get():
            status, patient = PatientController.find_by_unit_no(self.unit_no.get())
        else:
            messagebox.showerror("Select", "Select Patient")

    def refresh(self):
        status, patient_list = PatientController.find_all()
        if status:
            data_for_table = []
            for patient in patient_list:
                row = [patient.unit_no,patient.full_name, patient.father_name, patient.national_code, patient.birth_date,patient.phone_number, patient.age, patient.height, patient.weight,
                 patient.attending_physician, patient.kind_of_ad, patient.date_of_admission, patient.ward, patient.room,patient.bed, patient.notes_text ]
                data_for_table.append(row)
            self.table.refresh_table(data_for_table)
        else:
            self.table.clear_table()



