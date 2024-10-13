from view.component import EntryWithLabel
from controller.user_controller import UserController
from tkinter import *
from tkinter import messagebox as msg
# todo:

class UserView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sign up")
        self.window.geometry("400x500")
        self.name = EntryWithLabel(self.window,"Name", 20, 20, width=20)
        self.family = EntryWithLabel(self.window,"Family", 20, 60, width=20)
        self.mobile = EntryWithLabel(self.window,"Mobile", 20, 100, width=20)
        self.password = EntryWithLabel(self.window,"Password", 20, 140, width=20)
        # todo:



        Button(self.window, text="Save", width=7, command= self.save_click).place(x=20, y=300)
        Button(self.window, text="Remove", width=7, command= self.remove_click).place(x=100, y=300)
        Button(self.window, text="Edit", width=7, command= self.edit_click).place(x=180, y=300)


        self.window.mainloop()

    def save_click(self):
        status, message = UserController.save(self.mobile.get(),
                                              self.password.get(),
                                              self.name.get(),
                                              self.family.get())
        if status:
            msg.showinfo("Saved Successfully", message)
            #todo:
            from view.login_view import LoginView
            self.window.destroy()
            login_form = LoginView()

        else:
            msg.showerror("Save error", message)

    def edit_click(self):
        status, message = UserController.edit(self.mobile.get(),
                                              self.password.get(),
                                              self.name.get(),
                                              self.family.get())
        if status:
            msg.showinfo("Edit", message)
        else:
            msg.showerror("Edit error", message)

    def remove_click(self):
        status, message = UserController.remove(self.mobile.get())
        if status:
            msg.showinfo("Remove", message)
        else:
            msg.showerror("Remove error", message)










