from view import *
from controller.medical_record_contoroller import MedicalRecordController
from model.medical_record import MedicalRecord
# from tools.medical_record_validator import MedicalRecordValidator


class MedicalRecordView:
    def __init__(self,unit_no=None):
        self.unit_no = unit_no
        self.window = Tk()
        self.window.title("Medical Record Management")
        self.window.geometry("1400x800")

        self.record_id = LabelWithEntry(self.window, "Record ID",20,20, data_type=IntVar, state="readonly")
        self.unit_no =LabelWithEntry(self.window, "Unit No",20,80,data_type=IntVar )
        self.full_name = LabelWithEntry(self.window, "Full Name",20,140)
        self.date_of_admission = LabelWithEntry(self.window, "Admission Date",20,200)
        self.doctor_name =LabelWithEntry(self.window, "Doctor Name",20,260)
        self.staff_name = LabelWithEntry(self.window, "Staff Name",20,320)
        self.department_name =LabelWithEntry (self.window, "Department",20,380)
        self.session_type = LabelWithEntry(self.window, "Session Type",20,440)
        self.description = LabelWithEntry(self.window, "Description",20,500)
        self.medication = LabelWithEntry(self.window, "Medication",20,560)
        self.nursing_care = LabelWithEntry(self.window, "Nursing Care",20,620)
        self.lab_tests =LabelWithEntry (self.window, "Lab Tests",700,20)
        self.services =LabelWithEntry(self.window, "Services",700,80)
        self.total_amount=LabelWithEntry(self.window, "Total Amount",700,140,data_type=IntVar)
        self.payment_status=LabelWithEntry(self.window, "Payment Status",700,200,data_type=IntVar)
        self.table = Table(
            self.window,
            ["Record ID", "Unit No", "Full Name", "Admission", "Doctor", "Staff","Department", "Session", "Amount", "Payment"],
            [80, 80, 150, 100, 120, 120, 130, 100, 90, 90],
            0,0,
            15,
            self.select_from_table
        )
        Button(self.window, text="Save", width=15, command=self.save_click).place(x=700, y=700)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        try:

            record = MedicalRecord(self.record_id.get() ,self.unit_no.get(),self.full_name.get(),self.date_of_admission.get(),self.doctor_name.get(),self.staff_name.get(),self.department_name.get(),self.session_type.get(),self.description.get("1.0", "end").strip(),self.medication.get(),self.nursing_care.get(),self.lab_tests.get(),self.services.get(),self.total_amount.get(),self.payment_status.get())


            # validator = MedicalRecordValidator()
            # if not validator.validate(record):
            #     messagebox.showerror("Validation Error", validator.get_errors())
            #     return
            #
            #
            status, message = MedicalRecordController.save(record)
            if status:
                messagebox.showinfo("Success", "Medical Record Saved")
                self.clear_form()
                self.refresh_table()
            else:
                messagebox.showerror("Error", message)
        except Exception as e:
            messagebox.showerror("Error", e)

    def select_from_table(self):
        selected = self.table.table.focus()
        if not selected:
            return
        values = self.table.table.item(selected, "values")
        if values:
            status, record_data = MedicalRecordController.find_by_id()
            if status:
                self.fill_form()

    def fill_form(self):
        self.record_id.clear()
        self.unit_no.clear()
        self.full_name.clear()
        self.date_of_admission.clear()
        self.doctor_name.clear()
        self.staff_name.clear()
        self.department_name.clear()
        self.session_type.clear()
        self.description.clear()
        self.medication.clear()
        self.lab_tests.clear()
        self.services.clear()
        self.total_amount.clear()
        self.payment_status.clear()

    def clear_form(self):
        for var in [self.record_id, self.unit_no, self.full_name, self.date_of_admission,
                    self.doctor_name, self.staff_name, self.department_name, self.session_type,
                    self.medication, self.nursing_care, self.lab_tests, self.services,
                    self.total_amount, self.payment_status]:
            var.set("")
        self.desc_text.delete("1.0", "end")

    def refresh_table(self):
        records = MedicalRecordController.find_all()
        data = []
        for r in records:
            data.append([
                r.record_id, r.unit_no, r.full_name, r.date_of_admission,
                r.doctor_name, r.staff_name, r.department_name, r.session_type,
                r.total_amount, r.payment_status
            ])
        self.table.refresh_table(data)

