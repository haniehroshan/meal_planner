from tkinter import *
import tkinter.messagebox as msg

from controller.user_controller import UserController
from view.component import EntryWithLabel
from PIL import Image, ImageTk

#todo:



class LoginView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")
        self.window.geometry("340x350")

        img = Image.open("view/images/login.png")
        img = ImageTk.PhotoImage(img)
        Label(self.window, image=img).place(x=78, y=20)

        self.mobile = EntryWithLabel(self.window, "Mobile", 20, 170, width=20)
        self.password = EntryWithLabel(self.window, "Password", 20, 210, width=20)

        Button(self.window, text="Login", width=8, command=self.login_click).place(x=100, y=270)
        Button(self.window, text="Signup", width=8, command=self.signup_click).place(x=190, y=270)

        self.window.mainloop()


    def login_click(self):
        status, user = UserController.find_by_mobile_and_password(self.mobile.get(), self.password.get())
        if status:
            self.window.destroy()
            from view.patientvisit_view import PatientVisitView
            patient_visit_view = PatientVisitView(user)
            # todo
        else:
            msg.showerror("Login", "Access Denied !!!")

    def signup_click(self):
        self.window.destroy()
        from view.user_view import UserView
        user_view = UserView()
        # todo

