from tkinter import *

from controller.patient_controller import PatientController
from view.component import EntryWithLabel
from view.meal_plan_view import MealPlanView
from tkinter import messagebox as msg


class PatientVisitView:
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title('Patient Visit')
        self.window.geometry('400x500')


        self.weight = EntryWithLabel(self.window, "Weight",  20, 20, width=10, data_type="float")
        self.height = EntryWithLabel(self.window, "Height", 20, 60, width=10,  data_type="float")
        self.age = EntryWithLabel(self.window, "Age", 20, 100, width=10,  data_type="int")

        Label(self.window, text="Gender").place(x=20, y=140)
        self.gender = StringVar()
        Radiobutton(self.window, text="Female", variable=self.gender, value="Female").place(x=100, y=140)
        Radiobutton(self.window, text="Male", variable=self.gender, value="Male").place(x=100, y=180)
        self.gender.set("Female")

        Label(self.window, text="BMI").place(x=20, y=210)


        Button(self.window, text="Save", width=7, command= self.save_click).place(x=20, y=300)
        Button(self.window, text="Remove", width=7, command= self.remove_click).place(x=100, y=300)
        Button(self.window, text="Edit", width=7, command= self.edit_click).place(x=180, y=300)
        Button(self.window, text="Next", width=7, command= self.next_click).place(x=260, y=300)


        
        self.window.mainloop()

        # todo: def save_click, ...

    def save_click(self):
        status, message = PatientController.save(self.weight.get(),
                                                 self.height.get(),
                                                 self.age.get(),
                                                 self.gender.get())
        if status:
            msg.showinfo("Save", message)
        else:
            msg.showerror("Save error", message)

    def edit_click(self):
        status, message = PatientController.edit(self.weight.get(),
                                                 self.height.get(),
                                                 self.age.get(),
                                                 self.gender.get())
        if status:
            msg.showinfo("Edit", message)
        else:
            msg.showerror("Edit error", message)


    def remove_click(self):
        status, message = PatientController.remove(self.weight.get(),
                                                   self.height.get(),
                                                   self.age.get(),
                                                   self.gender.get())
        if status:
            msg.showinfo("Remove", message)
        else:
            msg.showerror("Remove error", message)

    def next_click(self):
        # Destroy current window
        self.window.destroy()

        # Get the patient information entered in this form
        patient_data = {
            "weight": self.weight.get(),
            "height": self.height.get(),
            "age": self.age.get(),
            "gender": self.gender.get()
        }

        # Combine the user data (name, family, etc.) with patient-specific data
        from model.entity.patient import Patient
        patient = Patient(
            id=self.user.id,            # From the user object
            name=self.user.name,        # From the user object
            family=self.user.family,    # From the user object
            mobile=self.user.mobile,    # From the user object
            password=self.user.password, # From the user object

            # Additional patient data from the form
            patient_id=self.user.id,    # You can use the same id as patient_id
            weight=patient_data["weight"],
            height=patient_data["height"],
            age=patient_data["age"],
            gender=patient_data["gender"]
        )

        # Pass the patient object to MealPlanView
        mealplan = Tk()
        MealPlanView(mealplan, patient)
        mealplan.mainloop()


