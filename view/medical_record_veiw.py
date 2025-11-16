# view/medical_record_view.py
import tkinter as tk
from tkinter import ttk, messagebox
from controller.medical_record_controller import MedicalRecordController
from view.components.label_with_entry import LabelWithEntry
from view.components.table import Table
from model.medical_record import MedicalRecord
from tools.medical_record_validator import MedicalRecordValidator


class MedicalRecordView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Medical Record Management")
        self.geometry("1400x800")
        self.center_window()
        self.configure(bg="#f0f0f0")
        self.resizable(False, False)

        # متغیرهای فرم
        self.record_id = tk.StringVar()
        self.unit_no = tk.StringVar()
        self.full_name = tk.StringVar()
        self.date_of_admission = tk.StringVar()
        self.doctor_name = tk.StringVar()
        self.staff_name = tk.StringVar()
        self.department_name = tk.StringVar()
        self.session_type = tk.StringVar()
        self.description = tk.StringVar()
        self.medication = tk.StringVar()
        self.nursing_care = tk.StringVar()
        self.lab_tests = tk.StringVar()
        self.services = tk.StringVar()
        self.total_amount = tk.StringVar()
        self.payment_status = tk.StringVar()

        self.create_widgets()
        self.refresh_table()

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def create_widgets(self):
        # === چپ: جدول ===
        left_frame = tk.Frame(self, bg="#f0f0f0")
        left_frame.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=20)

        headings = [
            "Record ID", "Unit No", "Full Name", "Admission", "Doctor", "Staff",
            "Department", "Session", "Amount", "Payment"
        ]
        column_widths = [80, 80, 150, 100, 120, 120, 130, 100, 90, 90]

        self.table = Table(
            left_frame,
            headings=headings,
            column_widths=column_widths,
            x=0, y=0, height=28,
            function_name=self.select_from_table
        )

        # === راست: فرم ===
        right_frame = tk.Frame(self, bg="#f0f0f0", width=550)
        right_frame.pack(side="right", fill="y", padx=(10, 20), pady=20)
        right_frame.pack_propagate(False)

        form_canvas = tk.Canvas(right_frame, bg="#f0f0f0")
        form_scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=form_canvas.yview)
        scrollable_frame = tk.Frame(form_canvas, bg="#f0f0f0")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: form_canvas.configure(scrollregion=form_canvas.bbox("all"))
        )
        form_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        form_canvas.configure(yscrollcommand=form_scrollbar.set)

        form_canvas.pack(side="left", fill="both", expand=True)
        form_scrollbar.pack(side="right", fill="y")

        # فیلدهای فرم
        fields = [
            ("Record ID:", self.record_id, "int", "readonly"),
            ("Unit No:", self.unit_no, "int", "normal"),
            ("Full Name:", self.full_name, "str", "normal"),
            ("Admission Date:", self.date_of_admission, "str", "normal"),
            ("Doctor Name:", self.doctor_name, "str", "normal"),
            ("Staff Name:", self.staff_name, "str", "normal"),
            ("Department:", self.department_name, "str", "normal"),
            ("Session Type:", self.session_type, "str", "normal"),
        ]

        for i, (label, var, dtype, state) in enumerate(fields):
            LabelWithEntry(scrollable_frame, label, var, data_type=dtype, state=state).pack(pady=6, anchor="w")

        # توضیحات
        tk.Label(scrollable_frame, text="Description:", bg="#f0f0f0").pack(pady=(10, 2), anchor="w")
        self.desc_text = tk.Text(scrollable_frame, height=4, width=60)
        self.desc_text.pack(pady=2, anchor="w")

        # سایر فیلدها
        extra_fields = [
            ("Medication:", self.medication),
            ("Nursing Care:", self.nursing_care),
            ("Lab Tests:", self.lab_tests),
            ("Services:", self.services),
            ("Total Amount:", self.total_amount),
            ("Payment Status:", self.payment_status),
        ]

        for label, var in extra_fields:
            LabelWithEntry(scrollable_frame, label, var).pack(pady=6, anchor="w")

        # === دکمه Save ===
        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(side="bottom", pady=20)
        tk.Button(btn_frame, text="Save", width=15, bg="#FF9800", fg="white",
                  command=self.save_click).pack()

    def save_click(self):
        try:
            # ایجاد شیء MedicalRecord
            record = MedicalRecord(
                record_id=self.record_id.get() or None,
                unit_no=self.unit_no.get(),
                full_name=self.full_name.get(),
                date_of_admission=self.date_of_admission.get(),
                doctor_name=self.doctor_name.get(),
                staff_name=self.staff_name.get(),
                department_name=self.department_name.get(),
                session_type=self.session_type.get(),
                description=self.desc_text.get("1.0", "end").strip(),
                medication=self.medication.get(),
                nursing_care=self.nursing_care.get(),
                lab_tests=self.lab_tests.get(),
                services=self.services.get(),
                total_amount=self.total_amount.get(),
                payment_status=self.payment_status.get()
            )

            # اعتبارسنجی
            validator = MedicalRecordValidator()
            if not validator.validate(record):
                messagebox.showerror("Validation Error", validator.get_errors())
                return

            # ذخیره
            status, message = MedicalRecordController.save(record.to_dict())
            if status:
                messagebox.showinfo("Success", "Medical Record Saved")
                self.clear_form()
                self.refresh_table()
            else:
                messagebox.showerror("Error", message)
        except Exception as e:
            messagebox.showerror("Error", f"Save failed: {str(e)}")

    def select_from_table(self, event):
        selected = self.table.table.focus()
        if not selected:
            return
        values = self.table.table.item(selected, "values")
        if values:
            status, record_data = MedicalRecordController.find_by_record_id(values[0])
            if status:
                self.fill_form(record_data)

    def fill_form(self, data):
        self.record_id.set(data.get("record_id", ""))
        self.unit_no.set(data.get("unit_no", ""))
        self.full_name.set(data.get("full_name", ""))
        self.date_of_admission.set(data.get("date_of_admission", ""))
        self.doctor_name.set(data.get("doctor_name", ""))
        self.staff_name.set(data.get("staff_name", ""))
        self.department_name.set(data.get("department_name", ""))
        self.session_type.set(data.get("session_type", ""))
        self.desc_text.delete("1.0", "end")
        self.desc_text.insert("1.0", data.get("description", ""))
        self.medication.set(data.get("medication", ""))
        self.nursing_care.set(data.get("nursing_care", ""))
        self.lab_tests.set(data.get("lab_tests", ""))
        self.services.set(data.get("services", ""))
        self.total_amount.set(data.get("total_amount", ""))
        self.payment_status.set(data.get("payment_status", ""))

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


# Test
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = MedicalRecordView(root)
    app.mainloop()
