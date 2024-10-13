from tkinter import *
from tkinter import ttk
from controller.food_controller import FoodController
from controller.meal_paln_controller import MealPlanController
from model.database.food_da import FoodDa
from bl.nutrition_calculator import NutritionCalculator
from tkinter import messagebox
from view.component import EntryWithLabel
from model.entity.patient import Patient


class MealPlanView:
    def __init__(self, win, patient, plan_id):
        self.plan_id = plan_id
        self.plan_info = EntryWithLabel(win, 'Plan Info', 300, 100, width=32, distance=100, data_type="str")
        self.win = win
        self.win.title("Meal Plan")
        self.win.geometry("1300x650")

        self.patient = patient
        self.all_meals = {}

        # total consumed calories and macronutrients
        self.total_calories_consumed = 0
        self.total_carbohydrates_consumed = 0
        self.total_protein_consumed = 0
        self.total_fat_consumed = 0

        # Entries for percentages
        self.carbohydrate_percentage = EntryWithLabel(win, "Carb(%)", 20, 50, width=15, data_type="int")
        self.protein_percentage = EntryWithLabel(win, "Protein(%)", 300, 50, distance=100, width=15, data_type="int")
        self.fat_percentage = EntryWithLabel(win, "Fat(%)", 640, 50, distance=100, width=15, data_type="int")



        # Meal label and Combobox
        Label(win, text="Meal").place(x=20, y=150)
        self.meal = StringVar()
        self.meal_combobox = ttk.Combobox(win, width=13,
                                          values=["Breakfast", "Snack 1", "Lunch", "Snack 2", "Dinner", "Snack3"])
        self.meal_combobox.place(x=100, y=150)

        # Food Name label and Combobox
        Label(win, text="Food Name").place(x=300, y=150)
        self.food_name = StringVar()
        self.food_combobox = ttk.Combobox(win, width=30)
        self.food_combobox.place(x=400, y=150)
        self.food_combobox.bind("<<ComboboxSelected>>", self.update_nutritional_values)
        FoodController.load_food_items()
        food_names = [food[0] for food in FoodController.load_food_items()]
        self.food_combobox['values'] = food_names
        self.food_combobox.bind('<KeyRelease>', self.update_food_combobox)

        # Entry for quantity
        self.quantity = EntryWithLabel(win, "Quantity(g)", 740, 150, distance=100, width=15, data_type="int")

        self.tree = ttk.Treeview(win, columns=("Meal", "Foods", "Quantity"), show='headings')
        self.tree.heading("Meal", text="Meal")
        self.tree.heading("Foods", text="Foods")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.column("Meal", width=200)
        self.tree.column("Foods", width=700)
        self.tree.column("Quantity", width=200)
        self.tree.place(x=80, y=200)

        self.save_button = Button(win, text="Save", bg="lightblue", width=10, command=self.save_meal)
        self.save_button.place(x=350, y=550)
        self.edit_button = Button(win, text="Edit", bg="lightblue", width=10, command=self.edit_meal)
        self.edit_button.place(x=500, y=550)
        self.remove_button = Button(win, text="Remove", bg="lightblue", width=10, command=self.remove_meal)
        self.remove_button.place(x=650, y=550)

    def update_food_combobox(self, event):
        current_input = self.food_combobox.get()
        food_options = FoodDa().find_by_food_name(current_input)

        food_names = [option[0] for option in food_options]
        self.food_combobox['values'] = food_names
        self.food_combobox.focus_set()



    def update_nutritional_values(self, event):
        selected_food = self.food_combobox.get()
        if selected_food:
            nutritional_values = FoodController.fetch_nutritional_values(selected_food)
            if nutritional_values:
                food_amount, food_calorie, food_carbohydrate, food_protein, food_fat = nutritional_values



    def reset_form(self):
        self.meal_combobox.set("")
        self.food_combobox.set("")
        self.quantity.set(0)
        self.meal_combobox.focus_set()

    # def refresh_table(self):
    #     for i in self.tree.get_children():
    #         self.tree.delete(i)
    #     for meal, foods in self.all_meals.items():
    #         self.tree.insert('', 'end', values=(meal, ', '.join(foods)))
    def refresh_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for meal, food_items in self.all_meals.items():
            for food, quantity in food_items:
                self.tree.insert('', 'end', values=(meal, food, f"{quantity}g"))

    def save_meal(self):
        # Step 1: Get the selected food, meal, and quantity
        selected_food = self.food_combobox.get()
        meal = self.meal_combobox.get()
        quantity = self.quantity.get()

        if selected_food and meal and quantity:
            # Create an object from NutritionCalculator
            calculator = NutritionCalculator(
                self.patient,
                float(self.carbohydrate_percentage.get()) / 100,
                float(self.protein_percentage.get()) / 100,
                float(self.fat_percentage.get()) / 100
            )
            self.calorie_needed = calculator.calorie_needed()
            self.carbohydrate_needed = calculator.carbohydrate_needed()
            self.protein_needed = calculator.protein_needed()
            self.fat_needed = calculator.fat_needed()

            # Fetch nutritional values
            nutritional_values = FoodController.fetch_nutritional_values(selected_food)
            if nutritional_values:
                food_amount, food_calorie, food_carbohydrate, food_protein, food_fat = nutritional_values

                # Calculate the nutritional values for the added food
                added_calories = (food_calorie * quantity) / food_amount
                added_carbohydrates = (food_carbohydrate * quantity) / food_amount
                added_protein = (food_protein * quantity) / food_amount
                added_fat = (food_fat * quantity) / food_amount

                # Update total consumed values
                self.total_calories_consumed += added_calories
                self.total_carbohydrates_consumed += added_carbohydrates
                self.total_protein_consumed += added_protein
                self.total_fat_consumed += added_fat

                # Calculate remaining nutritional values
                calorie_left = self.calorie_needed - self.total_calories_consumed
                carbohydrate_left = self.carbohydrate_needed - self.total_carbohydrates_consumed
                protein_left = self.protein_needed - self.total_protein_consumed
                fat_left = self.fat_needed - self.total_fat_consumed

                # Check if adding the food exceeds the needs
                if calorie_left >= 0 and carbohydrate_left >= 0 and protein_left >= 0 and fat_left >= 0:
                    # Add food to the all_meals dictionary with quantity
                    # if meal not in self.all_meals:
                    #     self.all_meals[meal] = []
                    # self.all_meals[meal].append(f"{selected_food} ({quantity}g)")
                    if meal not in self.all_meals:
                        self.all_meals[meal] = []
                    self.all_meals[meal].append((selected_food, quantity))

                    self.refresh_table()

                    # Show information for the added food and the remaining values
                    messagebox.showinfo("Nutritional Information",
                                        f"Added:\n"
                                        f"Calories: {added_calories:.2f}\n"
                                        f"Carbohydrates: {added_carbohydrates:.2f}\n"
                                        f"Protein: {added_protein:.2f}\n"
                                        f"Fat: {added_fat:.2f}\n\n"
                                        f"Remaining:\n"
                                        f"Calories left: {calorie_left:.2f}\n"
                                        f"Carbohydrates left: {carbohydrate_left:.2f}\n"
                                        f"Protein left: {protein_left:.2f}\n"
                                        f"Fat left: {fat_left:.2f}")

                    # Step 2: Prepare to save meal plan into MySQL
                    # # Format the foods string
                    # formatted_foods = [f"{food} ({quantity}g)" for food in self.all_meals.get(meal, [])]

                    # Step 3: Insert into MySQL table without quantity as a parameter
                    # status, message = MealPlanController.insert_data(
                    #     patient_id=self.patient.id,
                    #     plan_info=self.plan_info.get(),
                    #     calorie_needed=self.calorie_needed,
                    #     carbohydrate_percentage=float(self.carbohydrate_percentage.get()) / 100,
                    #     protein_percentage=float(self.protein_percentage.get()) / 100,
                    #     fat_percentage=float(self.fat_percentage.get()) / 100,
                    #     carbohydrate_needed=self.carbohydrate_needed,
                    #     protein_needed=self.protein_needed,
                    #     fat_needed=self.fat_needed,
                    #     meal=meal,
                    #     foods=
                    #
                    #     # foods=formatted_foods
                    # )
                    status, message = MealPlanController.insert_data(
                        patient_id=self.patient.id,
                        plan_info=self.plan_info.get(),
                        calorie_needed=self.calorie_needed,
                        carbohydrate_percentage=float(self.carbohydrate_percentage.get()) / 100,
                        protein_percentage=float(self.protein_percentage.get()) / 100,
                        fat_percentage=float(self.fat_percentage.get()) / 100,
                        carbohydrate_needed=self.carbohydrate_needed,
                        protein_needed=self.protein_needed,
                        fat_needed=self.fat_needed,
                        meal=meal,
                        foods=selected_food,  # This stores the food name
                        quantity=quantity
                    )

                    if status:
                        messagebox.showinfo("Save Meal", "Meal plan saved successfully.")
                    else:
                        messagebox.showerror("Save Error", f"Failed to save meal: {message}")

                    self.reset_form()
                else:
                    exceeded_nutrients = []

                    # Check which one exceeded the needs
                    if calorie_left < 0:
                        exceeded_nutrients.append(f"Calories ({added_calories:.2f})")
                    if carbohydrate_left < 0:
                        exceeded_nutrients.append(f"Carbohydrates ({added_carbohydrates:.2f})")
                    if protein_left < 0:
                        exceeded_nutrients.append(f"Protein ({added_protein:.2f})")
                    if fat_left < 0:
                        exceeded_nutrients.append(f"Fat ({added_fat:.2f})")

                    # Show a message listing the exceeded nutrients
                    exceeded_message = ", ".join(exceeded_nutrients)
                    messagebox.showwarning("Nutritional Limits Exceeded",
                                           f"Adding this food exceeds your daily "
                                           f"nutritional goals:\n{exceeded_message}")
                    self.reset_form()
            else:
                messagebox.showerror("Error", "Could not fetch nutritional values for the selected food.")
        else:
            messagebox.showwarning("Input Error", "Please select a food, meal, and quantity.")

    def edit_meal(self):
        meal = self.meal_combobox.get()
        selected_food = self.food_combobox.get()
        quantity = self.quantity.get()

        if meal and selected_food and quantity:
            status, message = MealPlanController.edit(
                patient_id=self.patient.id,
                plan_id=self.plan_id,
                meal=meal,
                foods=selected_food,  # Pass the food name
                quantity=quantity  # Pass the quantity for update
            )

            if status:
                messagebox.showinfo("Edit Meal", "Meal plan updated successfully.")
                self.refresh_table()
            else:
                messagebox.showerror("Edit Error", f"Failed to edit meal: {message}")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def remove_meal(self):
        meal = self.meal_combobox.get()
        selected_food = self.food_combobox.get()

        if meal and selected_food:
            status, message = MealPlanController.remove(
                patient_id=self.patient.id,
                plan_id=self.plan_id,
                meal=meal
            )

            if status:
                messagebox.showinfo("Remove Meal", "Meal plan removed successfully.")
                self.refresh_table()
            else:
                messagebox.showerror("Remove Error", f"Failed to remove meal: {message}")
        else:
            messagebox.showwarning("Warning", "Please select a meal and food to remove.")


if __name__ == "__main__":
    win = Tk()

    # Sample patient data
    patient = Patient(3, 3, "payman", "roshan", "09122110871", "pr09122110871", 105, 186, 42, "male")
    application = MealPlanView(win, patient, plan_id=None)
    win.mainloop()
