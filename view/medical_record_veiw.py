
import tkinter as tk
from tkinter import ttk, messagebox
from controller.medical_record_controller import MedicalRecordController
from view.components.label_with_entry import LabelWithEntry
from view.components.table import Table


class MedicalRecordView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Medical Record Management")
        self.geometry("1200x700")
        self.configure(bg="#f0f0f0")
        self.resizable(False, False)
        self.center_window()

        self.unit_no = tk.StringVar()
        self.full_name = tk.StringVar()
        self.doctor_name = tk.StringVar()
        self.staff_name = tk.StringVar()
        self.department_name = tk.StringVar()
        self.session_type = tk.StringVar()
        self.description = tk.StringVar()

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
        
        form_frame = tk.Frame(self, bg="#f0f0f0")
        form_frame.pack(pady=15, padx=20, fill="x")

        
        LabelWithEntry(form_frame, "Unit No:", self.unit_no, data_type="int", state="readonly",
                       x=20, y=20).place(x=20, y=20)
        LabelWithEntry(form_frame, "Patient Name:", self.full_name, state="readonly",
                       x=20, y=80).place(x=20, y=80)
        LabelWithEntry(form_frame, "Doctor Name:", self.doctor_name, state="readonly",
                       x=20, y=140).place(x=20, y=140)

        
        LabelWithEntry(form_frame, "Nurse Name:", self.staff_name, state="readonly",
                       x=20, y=200).place(x=20, y=200)
        LabelWithEntry(form_frame, "Department:", self.department_name, state="readonly",
                       x=20, y=260).place(x=20, y=260)
        LabelWithEntry(form_frame, "Session Type:", self.session_type,
                       x=20, y=320).place(x=20, y=320)

        
        tk.Label(form_frame, text="Description:", bg="#f0f0f0", anchor="e", width=15).place(x=20, y=380)
        self.desc_text = tk.Text(form_frame, height=4, width=80)
        self.desc_text.place(x=180, y=380)

        
        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        headings = ["Unit No", "Patient", "Doctor", "Nurse", "Department", "Session", "Date"]
        column_widths = [100, 180, 150, 150, 150, 120, 100]

        self.table = Table(
            table_frame,
            headings=headings,
            column_widths=column_widths,
            x=0, y=0, height=15,
            function_name=self.select_from_table
        )

        
        btn_frame = tk.Frame(self, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Select Record", width=15, bg="#2196F3", fg="white",
                  command=self.select_record).place(x=20, y=550)
        tk.Button(btn_frame, text="Refresh", width=12, bg="#4CAF50", fg="white",
                  command=self.refresh_table).place(x=180, y=550)
        tk.Button(btn_frame, text="Save", width=12, bg="#FF9800", fg="white",
                  command=self.save_click).place(x=300, y=550)
        tk.Button(btn_frame, text="Edit", width=12, bg="#FFC107", fg="white",
                  command=self.edit_click).place(x=420, y=550)
        tk.Button(btn_frame, text="Delete", width=12, bg="#f44336", fg="white",
                  command=self.delete_click).place(x=540, y=550)
        tk.Button(btn_frame, text="Clear", width=12, bg="#9E9E9E", fg="white",
                  command=self.reset_form).place(x=660, y=550)

    def save_click(self):
        status, message = MedicalRecordController.save(
            unit_no=self.unit_no.get(),
            full_name=self.full_name.get(),
            doctor_name=self.doctor_name.get(),
            staff_name=self.staff_name.get(),
            department_name=self.department_name.get(),
            session_type=self.session_type.get(),
            description=self.desc_text.get("1.0", "end").strip()
        )
        if status:
            messagebox.showinfo("Success", "Medical Record Saved")
            self.reset_form()
            self.refresh_table()
        else:
            messagebox.showerror("Error", "Medical Record Save Error")

    def edit_click(self):
        if not self.unit_no.get():
            messagebox.showerror("Error", "Select a record first")
            return
        status, message = MedicalRecordController.update(
            unit_no=self.unit_no.get(),
            full_name=self.full_name.get(),
            doctor_name=self.doctor_name.get(),
            staff_name=self.staff_name.get(),
            department_name=self.department_name.get(),
            session_type=self.session_type.get(),
            description=self.desc_text.get("1.0", "end").strip()
        )
        if status:
            messagebox.showinfo("Success", "Medical Record Updated")
            self.reset_form()
            self.refresh_table()
        else:
            messagebox.showerror("Error", "Medical Record Update Error")

    def delete_click(self):
        if not self.unit_no.get():
            messagebox.showerror("Error", "Select a record first")
            return
        if messagebox.askyesno("Confirm", "Delete this medical record?"):
            status, message = MedicalRecordController.delete(self.unit_no.get())
            if status:
                messagebox.showinfo("Success", "Medical Record Deleted")
                self.reset_form()
                self.refresh_table()
            else:
                messagebox.showerror("Error", "Medical Record Delete Error")

    def reset_form(self):
        self.unit_no.set("")
        self.full_name.set("")
        self.doctor_name.set("")
        self.staff_name.set("")
        self.department_name.set("")
        self.session_type.set("")
        self.desc_text.delete("1.0", "end")
        self.table.clear_table()

    def refresh_table(self):
        record_list = MedicalRecordController.find_all()
        data_for_table = []
        for rec in record_list:
            data_for_table.append([
                rec.unit_no,
                rec.full_name,
                rec.doctor_name,
                rec.staff_name,
                rec.department_name,
                rec.session_type,
                rec.visit_date
            ])
        self.table.refresh_table(data_for_table)

    def select_from_table(self, event):
        selected = self.table.table.focus()
        if not selected:
            return
        values = self.table.table.item(selected, "values")
        if values:
            status, record = MedicalRecordController.find_by_unit_no(values[0])
            if status:
                self.unit_no.set(record.unit_no)
                self.full_name.set(record.full_name)
                self.doctor_name.set(record.doctor_name)
                self.staff_name.set(record.staff_name)
                self.department_name.set(record.department_name)
                self.session_type.set(record.session_type)
                self.desc_text.delete("1.0", "end")
                self.desc_text.insert("1.0", record.description)

    def select_record(self):
        if not self.unit_no.get():
            messagebox.showerror("Error", "Select a record first")
            return
        status, record = MedicalRecordController.find_by_unit_no(self.unit_no.get())
        if status:
            messagebox.showinfo("Selected", f"Selected Record: {record.full_name}")
        else:
            messagebox.showerror("Error", "Record not found")



        



