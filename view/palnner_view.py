from tkinter import *
from view.component import EntryWithLabel
# from controller. import 
# from tkinter import messagebox as msg
from tkinter import ttk
# todo: table
class PlannerView():
    def __init__(self):
        self.window = Tk()
        self.window.geometry('800x800')
        self.window.title('Planner')

        Label(self.window, text="Food Name").place(x=20, y=20)
        self.food_name = StringVar()
        #todo: make foodcontroller and import FoodController.find_by_food_name from food database for values=
        # ttk.Combobox(self.window, textvariable=self.food_name,
        # values=Controller.find_by_food_name).place(x=20, y=50)

        self.food_amount = EntryWithLabel(self.window, "Amount", 80, 50, data_type="int")

        # If user enters serving size, it must be converted to grams and then searched
        # Label(self.window, text="Amount").place(x=80, y=50)
        # self.food_amount = IntVar()
        # ttk.Combobox(self.window, textvariable=self.food_amount, values=[find_serving_size]).place(x=20, y=80)

        # Button(self.window, text="Save", width=7, command= self.save_click).place(x=20, y=300)
        # Button(self.window, text="Remove", width=7, command= self.remove_click).place(x=100, y=300)
        # Button(self.window, text="Edit", width=7, command= self.edit_click).place(x=180, y=300)

        self.window.mainloop()

        # todo: def save_click, ... Dar FoodController.save begim if carb,gheire az carb, gheire morede niaz
        # kamtar bood save shavad va namayeshe meghdare baghi mande ba seda zadane tabe an dar in safhe

        # def save_click(self):
        #     status, message = FoodController.save(self.food_name.get(),
        #                                           self.food_amount.get())
        #     if status:
        #         msg.showinfo("Save", message)
            # else:
            #     msg.showerror("Save error", message)

        # def edit_click(self):
        #     status, message = FoodController.edit(self.food_name.get(),
        #         #                                           self.food_amount.get())
        #     if status:
        #         msg.showinfo("Edit", message)
        #     else:
        #         msg.showerror("Edit error", message)

        # def remove_click(self):
        #     status, message = FoodController.remove(self.food_name.get())
        #     if status:
        #         msg.showinfo("Remove", message)
        #     else:
        #         msg.showerror("Remove error", message)





