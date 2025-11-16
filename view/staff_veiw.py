from view import *
from model import Staff
from controller.staff_controller import StaffController


class StaffView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x720")
        self.window.title("Staff Management")

        self.staff_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.full_name = LabelWithEntry(self.window, "Full Name", 20, 60)
        self.father_name = LabelWithEntry(self.window, "Father Name", 20, 100)
        self.national_code = LabelWithEntry(self.window, "National Code", 20, 140, data_type=IntVar)
        self.personal_id_no = LabelWithEntry(self.window, "Personal Id No", 20, 180, data_type=IntVar)
        self.degree = LabelWithEntry(self.window, "Degree", 20, 220)
        self.birth_date = LabelWithEntry(self.window, "Birth Date", 20, 260)
        self.age = LabelWithEntry(self.window, "Age", 20, 300, data_type=IntVar)
        self.phone_number = LabelWithEntry(self.window, "Phone Number", 20, 340)
        self.address = LabelWithEntry(self.window, "Address", 20, 380)
        self.username = LabelWithEntry(self.window, "Username", 20, 420)
        self.password = LabelWithEntry(self.window, "Password", 20, 460)
        self.ward = LabelWithEntry(self.window, "Ward", 20, 500)
        self.role = LabelWithEntry(self.window, "Role", 20, 540)

        self.table = Table(
            self.window,
            ["Id", "Full Name", "Father Name", "National Code", "Personal Id No", "Degree",
             "Birth Date", "Age", "Phone Number", "Address", "Username", "Password","Ward", "Role"],
            [60, 120, 100, 110, 100, 80, 50, 110, 80,80],
            500, 20,
            28,
            self.select_from_table
        )

        Button(self.window, text="Select Staff", width=15, command=self.select_doctor).place(x=20, y=600)
        Button(self.window, text="Refresh", width=12, command=self.refresh).place(x=180, y=600)
        Button(self.window, text="Save", width=12, command=self.save_click).place(x=300, y=600)
        Button(self.window, text="Edit", width=12, command=self.edit_click).place(x=420, y=600)
        Button(self.window, text="Delete", width=12, command=self.delete_click).place(x=540, y=600)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = StaffController.save(
            self.staff_id.get(),
            self.full_name.get(),
            self.father_name.get(),
            self.national_code.get(),
            self.personal_id_no.get(),
            self.degree.get(),
            self.birth_date.get(),
            self.age.get(),
            self.phone_number.get(),
            self.address.get(),
            self.username.get(),
            self.password.get(),
            self.ward.get(),
            self.role.get())
        if status:
            messagebox.showinfo("Staff Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Staff Save Error", message)

    def edit_click(self):
        status, message = StaffController.update(self.staff_id.get(), self.full_name.get(),
                                                   self.father_name.get(),
                                                  self.national_code.get(), self.personal_id_no.get(),
                                                  self.degree.get(), self.birth_date.get(), self.age.get(),
                                                  self.phone_number.get(), self.address.get(), self.username.get(),
                                                  self.password.get(),self.ward.get(),self.role.get())
        if status:
            messagebox.showinfo("Staff Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Staff Update Error", message)

    def delete_click(self):
        status, message = StaffController.delete(self.Staff_id.get())
        if status:
            messagebox.showinfo("Staff Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Staff Delete Error", message)

    def reset_form(self):
        self.staff_id.clear()
        self.full_name.clear()
        self.father_name.clear()
        self.national_code.clear()
        self.personal_id_no.clear()
        self.degree.clear()
        self.birth_date.clear()
        self.age.clear()
        self.address.clear()
        self.phone_number.clear()
        self.username.clear()
        self.password.clear()
        self.ward.clear()
        self.role.clear()
        status, staff_list = StaffController.find_all()
        self.table.refresh_table(staff_list)

    def select_from_table(self, selected_staff):
        if selected_staff:
            status, staff = StaffController.find_by_id(selected_staff[0])
            if status:
                staff = Staff(*selected_staff)
                self.staff_id.set(staff.doctor_id)
                self.full_name.set(staff.full_name)
                self.father_name.set(staff.father_name)
                self.national_code.set(staff.national_code)
                self.personal_id_no.set(staff.personal_id_no)
                self.degree.set(staff.degree)
                self.birth_date.set(staff.birth_date)
                self.age.set(staff.age)
                self.address.set(staff.address)
                self.phone_number.set(staff.phone_number)
                self.username.set(staff.username)
                self.password.set(staff.password)
                self.ward.set(staff.ward)
                self.role.set(staff.role)

    def select_staff(self):
        if self.staff_id.get():
            status, staff = StaffController.find_by_id(self.staff_id.get())
        else:
            messagebox.showerror("Select", "Select Staff")

    def refresh(self):
        status, staff_list = StaffController.find_all()
        if status:
            data_for_table = []
            for staff in staff_list:
                row = [staff.staff_id,staff.full_name, staff.father_name, staff.national_code, staff.personal_id_no, staff.degree, staff.birth_date, staff.age, staff.phone_number,
                 staff.address, staff.username, staff.password, staff.ward, staff.role]
                data_for_table.append(row)
            self.table.refresh_table(data_for_table)
        else:
            self.table.clear_table()



