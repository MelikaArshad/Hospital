from view import *
from model import Department
from controller.department_contoroller import DepartmentController

class DepartmentView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("920x550")
        self.window.title("Department Management")

        self.department_id = LabelWithEntry(self.window, "Id", 20,20, data_type=IntVar, state="readonly")
        self.department_name= LabelWithEntry(self.window, "Department Name", 20,80)
        self.department_controller= LabelWithEntry(self.window, "Department Controller", 20,140)

        self.table = Table(
            self.window,
            ["Id","Department Name","Department Controller" ],
            [80,200,200],
            400,20,
            20,
            self.select_from_table
        )

        Button(self.window, text="Select Department", width=18, command=self.select_department).place(x=20, y=500)
        Button(self.window, text="Refresh", width=12, command=self.refresh).place(x=200, y=500)
        Button(self.window, text="Save", width=12, command=self.save_click).place(x=320, y=500)
        Button(self.window, text="Edit", width=12, command=self.edit_click).place(x=440, y=500)
        Button(self.window, text="Delete", width=12, command=self.delete_click).place(x=560, y=500)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message= DepartmentController.save(self.department_id.get(), self.department_name.get(), self.department_controller.get())
        if status:
            messagebox.showinfo("Department Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Department Save Error", message)
    def edit_click(self):
        status, message= DepartmentController.update(self.department_id.get(), self.department_name.get(), self.department_controller.get())
        if status:
            messagebox.showinfo("Department Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Department Update Error", message)
    def delete_click(self):
        status, message= DepartmentController.delete(self.department_id.get())
        if status:
            messagebox.showinfo("Department Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Department Delete Error", message)
    def reset_form(self):
        self.department_id.clear()
        self.department_name.clear()
        self.department_controller.clear()
        status, department_list = DepartmentController.find_all()
        self.table.refresh_table(department_list)

    def select_from_table(self, selected_department):
        if selected_department:
            status, department = DepartmentController.find_by_id(selected_department[0])
            if status:
                department = Department(*selected_department)
                self.department_id.set(department.department_id)
                self.department_name.set(department.department_name)
                self.department_controller.set(department.department_controller)

    def select_department(self):
        if self.department_id.get():
            status,department = DepartmentController.find_by_id(self.department_id.get())
        else:
            messagebox.showerror("Select", "Select Department")

    def refresh(self):
        status , department_list = DepartmentController.find_all()
        if status:
            data_for_table = []
            for department in department_list:
                row = [department.department_id,department.department_name,department.department_controller]
                data_for_table.append(row)
            self.table.refresh_table(data_for_table)
        else:
            self.table.clear_table()



