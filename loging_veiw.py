from view import *
from controller import StaffController
from model import Staff

class LoginView:
    def __init__(self):
        self.staff_controller =StaffController()
        self.window=Tk()
        self.window.title("Staff")
        self.window.config(background="white")
        self.window.geometry("300x500")

        image = Image.open("./view/images/user.png")
        image = ImageTk.PhotoImage(image)

        Label(self.window, image=image).place(x=50, y=15)

        self.username = LabelWithEntry(self.window,"Username",30,270)
        self.password = LabelWithEntry(self.window,"Password",30,310)

        self.username.set("Melika")
        self.password.set("1234pass")

        Button(self.window, text="Login", width=8,font=("Arial", 14), command=self.login).place(x=50, y=380, width=200,height=70)

        self.window.mainloop()


    def login(self):
        status, staff = self.staff_controller.find_by_national_code(self.username.get(), self.password.get())

        if status:
            self.window.destroy()
            Staff.staff = staff
            DashboardView()
        else:
            messagebox.showerror("Login Error", "Access Denied !!!")

