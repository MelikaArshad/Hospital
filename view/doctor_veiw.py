from view import *
from model import Doctor
from controller.doctor_controller import DoctorController

class DoctorView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1250x700")
        self.window.title("Doctor Management")

        self.doctor_id = LabelWithEntry(self.window, "Id", 20,20, data_type=IntVar, state="readonly")
        self.full_name= LabelWithEntry(self.window, "Full Name", 20,60)
        self.department_controller= LabelWithEntry(self.window, "Department Controller", 20,100)
        self.father_name = LabelWithEntry(self.window, "Father Name", 20, 140)
        self.national_code = LabelWithEntry(self.window, "National Code", 20, 180, data_type=IntVar)
        self.personal_id_no = LabelWithEntry(self.window, "Personal Id No", 20, 220, data_type=IntVar)
        self.degree = LabelWithEntry(self.window, "Degree", 20, 260)
        self.birth_date = LabelWithEntry(self.window, "Birth Date", 20, 300)
        self.age = LabelWithEntry(self.window, "Age", 20, 340, data_type=IntVar)
        self.phone_number = LabelWithEntry(self.window, "Phone Number", 20, 380)
        self.address = LabelWithEntry(self.window, "Address", 20, 420)
        self.username = LabelWithEntry(self.window, "Username", 20, 460)
        self.password = LabelWithEntry(self.window, "Password", 20, 500)

        self.table = Table(
            self.window,
            ["Id", "Full Name","Department Controller","Father Name","National Code","Personal Id No","Degree","Birth Date","Age","Phone Number","Address","Username","Password"],
            [60,120,100,90,100,100,80,50,110],
            520,20,
            28,
            self.select_from_table
        )

        Button(self.window, text="Select Doctor", width=15, command=self.select_doctor).place(x=20, y=600)
        Button(self.window, text="Refresh", width=12, command=self.refresh).place(x=180, y=600)
        Button(self.window, text="Save", width=12, command=self.save_click).place(x=300, y=600)
        Button(self.window, text="Edit", width=12, command=self.edit_click).place(x=420, y=600)
        Button(self.window, text="Delete", width=12, command=self.delete_click).place(x=540, y=600)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message= DoctorController.save(self.doctor_id.get(),self.full_name.get() ,self.department_controller.get(),self.father_name.get(), self.national_code.get(), self.personal_id_no.get(),self.degree.get(), self.birth_date.get(), self.age.get(),
                 self.phone_number.get(),self.address.get(), self.username.get(), self.password.get())
        if status:
            messagebox.showinfo("Doctor Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Doctor Save Error", message)
    def edit_click(self):
        status, message= DoctorController.update(self.doctor_id.get(),self.full_name.get() ,self.department_controller.get(),self.father_name.get(), self.national_code.get(), self.personal_id_no.get(),self.degree.get(), self.birth_date.get(), self.age.get(),
                 self.phone_number.get(),self.address.get(), self.username.get(), self.password.get())
        if status:
            messagebox.showinfo("Doctor Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Doctor Update Error", message)
    def delete_click(self):
        status, message= DoctorController.delete(self.doctor_id.get())
        if status:
            messagebox.showinfo("Doctor Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Doctor Delete Error", message)
    def reset_form(self):
        self.doctor_id.clear()
        self.full_name.clear()
        self.department_controller.clear()
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
        status, doctor_list = DoctorController.find_all()
        self.table.refresh_table(doctor_list)

    def select_from_table(self, selected_doctor):
        if selected_doctor:
            status, doctor = DoctorController.find_by_id(selected_doctor[0])
            if status:
                doctor = Doctor(*selected_doctor)
                self.doctor_id.set(doctor.doctor_id)
                self.full_name.set(doctor.full_name)
                self.department_controller.set(doctor.department_controller)
                self.father_name.set(doctor.father_name)
                self.national_code.set(doctor.national_code)
                self.personal_id_no.set(doctor.personal_id_no)
                self.degree.set(doctor.degree)
                self.birth_date.set(doctor.birth_date)
                self.age.set(doctor.age)
                self.address.set(doctor.address)
                self.phone_number.set(doctor.phone_number)
                self.username.set(doctor.username)
                self.password.set(doctor.password)


    def select_doctor(self):
        if self.doctor_id.get():
            status, doctor = DoctorController.find_by_id(self.doctor_id.get())
        else:
            messagebox.showerror("Select", "Select Doctor")

    def refresh(self):
        status , doctor_list = DoctorController.find_all()
        if status:
            data_for_table = []
            for doctor in doctor_list:
                row = [doctor.doctor_id, doctor.full_name, doctor.department_controller, doctor.father_name, doctor.national_code, doctor.personal_id_no, doctor.degree, doctor.birth_date, doctor.age,doctor.phone_number, doctor.address, doctor.username, doctor.password]
                data_for_table.append(row)
            self.table.refresh_table(data_for_table)
        else:
            self.table.clear_table()



