from tkinter import *
from view.component import EntryWithLabel
# from controller. import
# from tkinter import messagebox as msg
# todo:
# from view.planner_view import PlannerView

class PatientVisitView:
    def __init__(self):
        self.window = Tk()
        self.window.title('Patient Visit')
        self.window.geometry('400x500')


        self.weight = EntryWithLabel(self.window, "Weight", 20, 20, data_type="float")
        self.height = EntryWithLabel(self.window, "Height", 20, 60, data_type="float")
        self.age = EntryWithLabel(self.window, "Age", 20, 100, data_type="int")

        Label(self.window, text="Gender").place(x=20, y=140)
        self.gender = StringVar()
        Radiobutton(self.window, text="Female", variable=self.gender, value="Female").place(x=100, y=140)
        Radiobutton(self.window, text="Male", variable=self.gender, value="Male").place(x=100, y=180)
        self.gender.set("Female")

        # Label(self.window, text="BMI").place(x=20, y=210)


        # Button(self.window, text="Save", width=7, command= self.save_click).place(x=20, y=300)
        # Button(self.window, text="Remove", width=7, command= self.remove_click).place(x=100, y=300)
        # Button(self.window, text="Edit", width=7, command= self.edit_click).place(x=180, y=300)


        
        self.window.mainloop()

        # todo: def save_click, ...

        # def save_click(self):
        #     status, message = PatientVisitController.save(self.weight.get(),
        #                                           self.height.get(),
        #                                           self.age.get(),
        #                                           self.gender.get())
        #     if status:
        #         msg.showinfo("Save", message)
                # todo:
                # self.window.destroy()
                # planner = PlannerView()
            # else:
            #     msg.showerror("Save error", message)

        # def edit_click(self):
        #     status, message = PatientVisitController.edit(self.weight.get(),
        # #                                           self.height.get(),
        # #                                           self.age.get(),
        # #                                           self.gender.get())
        #     if status:
        #         msg.showinfo("Edit", message)
        #     else:
        #         msg.showerror("Edit error", message)

        # def remove_click(self):
        #     status, message = PatientVisitController.remove(self.)
        #     if status:
        #         msg.showinfo("Remove", message)
        #     else:
        #         msg.showerror("Remove error", message)
