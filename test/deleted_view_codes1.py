from tkinter import *
from tkinter import ttk
import mysql.connector
from controller.food_controller import FoodController
from model.database.food_da import FoodDa
from bl.nutrition_calculator import NutritionCalculator
class MealPlanView:
    def __init__(self, root):
        self.root = root
        self.root.title("Meal Plan")
        self.root.geometry("1500x700")

        self.all_meals = {}


        # meal label and Combobox
        Label(root, text="Meal").place(x=20, y=100)
        self.meal = StringVar()
        self.meal_combobox = ttk.Combobox(root, width=18,
                                          values=["Breakfast", "Snack 1", "Lunch", "Snack 2","Dinner", "Snack3"])
        self.meal_combobox.place(x=100, y=100)

        # food_name label and Combobox(values=options fetched from food database)
        Label(root, text="Food Name").place(x=300, y=100)
        self.food_name = StringVar()
        self.food_combobox = ttk.Combobox(root)
        self.food_combobox.place(x=400, y=100)
        self.food_combobox.bind("<<ComboboxSelected>>", self.update_serving_sizes)

        # Bind the key release event to update food options
        self.food_combobox.bind('<KeyRelease>', self.update_food_combobox)

        # todo : values for combobox from FoodDa
        # label and Combobox for food serving_size
        Label(root, text="Serving").place(x=640, y=100)
        self.serving_combobox = ttk.Combobox(root)
        self.serving_combobox.place(x=740, y=100)

        # quantity
        Label(root, text="Quantity").place(x=980, y=100)
        self.quantity = IntVar()
        Entry(root, textvariable=self.quantity, width=10).place(x=1080, y=100)


        # Save button
        self.save_button = Button(root, text="Save", width=10, command=self.save_meal)
        self.save_button.place(x=550, y=550)

        self.tree = ttk.Treeview(root, columns=("Meal", "Foods"), show='headings')
        self.tree.heading("Meal", text="Meal")
        self.tree.heading("Foods", text="Foods")
        self.tree.place(x=80, y=150)

        # entries for percentages
        Label(root, text="Carb(%)").place(x=20, y=50)
        self.carbohydrate_percentage = Entry(root)
        self.carbohydrate_percentage.place(x=100, y=50)

        Label(root, text="Protein(%)").place(x=300, y=50)
        self.protein_percentage = Entry(root)
        self.protein_percentage.place(x=400, y=50)

        Label(root, text="Fat(%)").place(x=640, y=50)
        self.fat_percentage = Entry(root)
        self.fat_percentage.place(x=740, y=50)

        # Add Food button
        self.add_button = Button(root, text="Add Food", command=self.add_food)
        self.add_button.place(x=1300, y=95)

        self.save_percentages_button = Button(root, text="Save Percentages", command=self.save_percentages)
        self.save_percentages_button.place(x=1300, y=45)

    def update_food_combobox(self, event):
        current_input = self.food_combobox.get()
        food_options = FoodDa().find_by_food_name(current_input)

        food_names = [option[0] for option in food_options]
        print("Food names:", food_names)  # Debug print

        self.food_combobox['values'] = food_names

        # Keep focus on the Combobox
        self.food_combobox.focus_set()

        # Open the dropdown if there are food names
        if food_names:
            self.food_combobox.event_generate('<Down>')

    def save_percentages(self):
        carbohydrate = float(self.carbohydrate_percentage.get()) / 100
        protein = float(self.protein_percentage.get()) / 100
        fat = float(self.fat_percentage.get()) / 100
        self.percentages = (carbohydrate, protein, fat)
        print(f"Saved percentages: carbohydrate: {carbohydrate}, Protein: {protein}, Fat: {fat}")

    def update_serving_sizes(self, event):
        selected_food = self.food_combobox.get()
        if selected_food:
            serving_sizes = self.fetch_serving_sizes(selected_food)
            self.serving_combobox['values'] = serving_sizes

    #todo
    def fetch_serving_sizes(self, food_name):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123',
            database='planner'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT serving_size FROM food_composition_tbl WHERE food_name = %s", (food_name,))
        serving_sizes = [row[0] for row in cursor.fetchall()]
        conn.close()
        return serving_sizes

    # todo
    def fetch_nutritional_values(self, food_name):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123',
            database='planner'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT food_calorie, food_carbohydrate, food_protein, food_fat FROM food_composition_tbl WHERE food_name = %s", (food_name,))
        nutritional_values = cursor.fetchone()
        conn.close()
        return nutritional_values

    # todo
    def insert_data(self, meal, foods):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123',
            database='planner'
        )
        cursor = conn.cursor()

        for food_name, serving_size in foods:
            cursor.execute(
                "INSERT INTO meal_plan_tbl (meal, food_name, serving_size) VALUES (%s, %s, %s)",
                (meal, food_name, serving_size)
            )

        conn.commit()
        conn.close()


    # todo
    def add_food(self):
        # Patient's nutritional needs
        self.calorie_needed = NutritionCalculator.calorie_needed
        self.carbohydrate_needed = NutritionCalculator.carbohydrate_needed
        self.protein_needed = NutritionCalculator.protein_needed
        self.fat_needed = NutritionCalculator.fat_needed

        selected_food = self.food_combobox.get()
        meal = self.meal_combobox.get()
        # todo
        serving = self.serving_combobox.get()  # Get the serving from the second combobox

        if selected_food and meal and serving:
            nutritional_values = self.fetch_nutritional_values(selected_food)
            if nutritional_values:
                food_calorie, food_carbohydrate, food_protein, food_fat = nutritional_values
                if (food_calorie <= self.calorie_needed and
                    food_carbohydrate <= self.carbohydrate_needed and
                    food_protein <= self.protein_needed and
                    food_fat <= self.fat_needed):
                    if meal not in self.all_meals:
                        self.all_meals[meal] = []
                    self.all_meals[meal].append(f"{selected_food} ({serving})")
                    self.update_treeview()
                else:
                    print("Nutritional values exceed patient's needs.")
            else:
                print("Nutritional values not found for the selected food.")

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for meal, foods in self.all_meals.items():
            foods_str = ', '.join(foods)
            self.tree.insert('', 'end', values=(meal, foods_str))

    def save_meal(self):
        meal = self.meal_combobox.get()
        if meal in self.all_meals:
            self.insert_data(meal, self.all_meals[meal])

if __name__ == "__main__":
    root = Tk()
    application = MealPlanView(root)
    root.mainloop()
