# from controller.patient_controller import PatientController
# from  model.entity.patient import Patient
#
#
# patient_data = PatientController.get_patient_data(3)
# print(patient_data)  # Debug: Print the fetched data
#
# # # Check if data is valid before proceeding
# # if patient_data:
# #     patient = Patient(
# #         patient_id=patient_data[0],
# #         weight=patient_data[1],
# #         height=patient_data[2],
# #         age=patient_data[3],
# #         gender=patient_data[4]
# #     )
# # else:
# #     print("No patient data found.")
#
#
#
#
#
# # Omitted from meal_plan_view:
# # def fetch_nutritional_values(self, food_name):
#     #     conn = mysql.connector.connect(
#     #         host='localhost',
#     #         user='root',
#     #         password='root123',
#     #         database='planner'
#     #     )
#     #     cursor = conn.cursor()
#     #     cursor.execute("SELECT food_amount, food_calorie, food_carbohydrate, food_protein, food_fat FROM food_composition_tbl WHERE food_name = %s", (food_name,))
#     #     nutritional_values = cursor.fetchone()
#     #     conn.close()
#     #     return nutritional_values
#
#     # def insert_data(self, meal, foods):
#     #     conn = mysql.connector.connect(
#     #         host='localhost',
#     #         user='root',
#     #         password='root123',
#     #         database='planner'
#     #     )
#     #     cursor = conn.cursor()
#     #
#     #     for food_name, quantity in foods:
#     #         cursor.execute(
#     #             "INSERT INTO meal_plan_tbl (meal, food_name, quantity) VALUES (%s, %s, %s)",
#     #             (meal, food_name, quantity)
#     #         )
#     #
#     #     conn.commit()
#     #     conn.close()
#
#
# # def load_food_items(self):
# #     """Fetch all food items from the database and populate the Combobox."""
# #     conn = mysql.connector.connect(
# #         host='localhost',
# #         user='root',
# #         password='root123',
# #         database='planner'
# #     )
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT food_name FROM food_composition_tbl")
# #     food_options = cursor.fetchall()
# #     conn.close()
#
#
# # in the view:
# # # Buttons
# # self.save_percentages_button = Button(win, text="Save Percentages And Continue",
# #                                       bg="pink", command=self.save_percentages)
# # self.save_percentages_button.place(x=1000, y=45)
#
# # self.add_button = Button(win, text="Add Food", bg="lightgreen", command=self.add_food)
# # self.add_button.place(x=1050, y=140)
# # self.edit_button = Button(win, text="Edit Food", bg="lightgreen", command=self.edit_food)
# # self.edit_button.place(x=1150, y=140)
# # self.remove_button = Button(win, text="Remove Food", bg="lightgreen", command=self.remove_food)
# # self.remove_button.place(x=1250, y=140)
# # def add_food(self):
#     #     # Create an object from NutritionCalculator
#     #     calculator = NutritionCalculator(
#     #         self.patient,
#     #         float(self.carbohydrate_percentage.get()) / 100,
#     #         float(self.protein_percentage.get()) / 100,
#     #         float(self.fat_percentage.get()) / 100
#     #     )
#     #     self.calorie_needed = calculator.calorie_needed()
#     #     self.carbohydrate_needed = calculator.carbohydrate_needed()
#     #     self.protein_needed = calculator.protein_needed()
#     #     self.fat_needed = calculator.fat_needed()
#     #
#     #     selected_food = self.food_combobox.get()
#     #     meal = self.meal_combobox.get()
#     #     quantity = self.quantity.get()
#     #
#     #     if selected_food and meal and quantity:
#     #         nutritional_values = FoodController.fetch_nutritional_values(selected_food)
#     #         if nutritional_values:
#     #             food_amount, food_calorie, food_carbohydrate, food_protein, food_fat = nutritional_values
#     #
#     #             # Calculate the nutritional values for the added food
#     #             added_calories = (food_calorie * quantity) / food_amount
#     #             added_carbohydrates = (food_carbohydrate * quantity) / food_amount
#     #             added_protein = (food_protein * quantity) / food_amount
#     #             added_fat = (food_fat * quantity) / food_amount
#     #
#     #             # Update total consumed values
#     #             self.total_calories_consumed += added_calories
#     #             self.total_carbohydrates_consumed += added_carbohydrates
#     #             self.total_protein_consumed += added_protein
#     #             self.total_fat_consumed += added_fat
#     #
#     #             # Calculate the remaining nutritional values
#     #             calorie_left = self.calorie_needed - self.total_calories_consumed
#     #             carbohydrate_left = self.carbohydrate_needed - self.total_carbohydrates_consumed
#     #             protein_left = self.protein_needed - self.total_protein_consumed
#     #             fat_left = self.fat_needed - self.total_fat_consumed
#     #
#     #             # Check if adding the food exceeds the needs
#     #             if calorie_left >= 0 and carbohydrate_left >= 0 and protein_left >= 0 and fat_left >= 0:
#     #                 if meal not in self.all_meals:
#     #                     self.all_meals[meal] = []
#     #                 self.all_meals[meal].append(f"{selected_food} ({quantity}:grams)")
#     #                 self.refresh_table()
#     #
#     #                 # Show information for the added food and the remaining values
#     #                 messagebox.showinfo("Nutritional Information",
#     #                                     f"Added:\n"
#     #                                     f"Calories: {added_calories:.2f}\n"
#     #                                     f"Carbohydrates: {added_carbohydrates:.2f}\n"
#     #                                     f"Protein: {added_protein:.2f}\n"
#     #                                     f"Fat: {added_fat:.2f}\n\n"
#     #                                     f"Remaining:\n"
#     #                                     f"Calories left: {calorie_left:.2f}\n"
#     #                                     f"Carbohydrates left: {carbohydrate_left:.2f}\n"
#     #                                     f"Protein left: {protein_left:.2f}\n"
#     #                                     f"Fat left: {fat_left:.2f}")
#     #                 self.reset_form()
#     #             else:
#     #                 exceeded_nutrients = []
#     #
#     #                 # Check which one exceeded the needs
#     #                 if calorie_left < 0:
#     #                     exceeded_nutrients.append(f"Calories ({added_calories:.2f})")
#     #                 if carbohydrate_left < 0:
#     #                     exceeded_nutrients.append(f"Carbohydrates ({added_carbohydrates:.2f})")
#     #                 if protein_left < 0:
#     #                     exceeded_nutrients.append(f"Protein ({added_protein:.2f})")
#     #                 if fat_left < 0:
#     #                     exceeded_nutrients.append(f"Fat ({added_fat:.2f})")
#     #
#     #                 #  show a message listing the exceeded nutrients
#     #                 exceeded_message = ", ".join(exceeded_nutrients)
#     #                 messagebox.showwarning("Nutritional Limits Exceeded",
#     #                                        f"Adding this food exceeds your daily "
#     #                                        f"nutritional goals:\n{exceeded_message}")
#     #                 self.reset_form()
#
# # def save_meal(self):
# #     meal = self.meal_combobox.get()
# #     foods = self.all_meals.get(meal, [])
# #
# #     # Format the foods with quantities
# #     quantity = self.quantity.get()
# #     formatted_foods = [f"{food} ({quantity}g)" for food in foods]
# #
# #     if meal and formatted_foods and quantity:
# #         carbohydrate_percentage = float(self.carbohydrate_percentage.get()) / 100
# #         protein_percentage = float(self.protein_percentage.get()) / 100
# #         fat_percentage = float(self.fat_percentage.get()) / 100
# #
# #         # Insert into MySql table
# #         status, message = MealPlanController.insert_data(
# #             patient_id=self.patient.id,
# #             plan_info=self.plan_info.get(),
# #             plan_id=self.plan_id,
# #             calorie_needed=self.calorie_needed,
# #             carbohydrate_percentage=carbohydrate_percentage,
# #             protein_percentage=protein_percentage,
# #             fat_percentage=fat_percentage,
# #             carbohydrate_needed=self.carbohydrate_needed,
# #             protein_needed=self.protein_needed,
# #             fat_needed=self.fat_needed,
# #             meal=meal,
# #             foods=formatted_foods
# #         )
# #
# #         if status:
# #             messagebox.showinfo("Save Meal", "Meal plan saved successfully.")
# #
# #         else:
# #             messagebox.showerror("Save Error", f"Failed to save meal: {message}")
#
# # def save_percentages(self):
# #     carbohydrate = float(self.carbohydrate_percentage.get()) / 100
# #     protein = float(self.protein_percentage.get()) / 100
# #     fat = float(self.fat_percentage.get()) / 100
# #     self.percentages = (carbohydrate, protein, fat)
# def save_meal(self):
#     # Step 1: Get the selected food, meal, and quantity
#     selected_food = self.food_combobox.get()
#     meal = self.meal_combobox.get()
#     quantity = self.quantity.get()
#
#     if selected_food and meal and quantity and self.carbohydrate_percentage and self.protein_percentage and self.fat_percentage:
#         # Create an object from NutritionCalculator
#         calculator = NutritionCalculator(
#             self.patient,
#             float(self.carbohydrate_percentage.get()) / 100,
#             float(self.protein_percentage.get()) / 100,
#             float(self.fat_percentage.get()) / 100
#         )
#         self.calorie_needed = calculator.calorie_needed()
#         self.carbohydrate_needed = calculator.carbohydrate_needed()
#         self.protein_needed = calculator.protein_needed()
#         self.fat_needed = calculator.fat_needed()
#
#         # Fetch nutritional values
#         nutritional_values = FoodController.fetch_nutritional_values(selected_food)
#         if nutritional_values:
#             food_amount, food_calorie, food_carbohydrate, food_protein, food_fat = nutritional_values
#
#             # Calculate the nutritional values for the added food
#             added_calories = (food_calorie * quantity) / food_amount
#             added_carbohydrates = (food_carbohydrate * quantity) / food_amount
#             added_protein = (food_protein * quantity) / food_amount
#             added_fat = (food_fat * quantity) / food_amount
#
#             # Update total consumed values
#             self.total_calories_consumed += added_calories
#             self.total_carbohydrates_consumed += added_carbohydrates
#             self.total_protein_consumed += added_protein
#             self.total_fat_consumed += added_fat
#
#             # Calculate remaining nutritional values
#             calorie_left = self.calorie_needed - self.total_calories_consumed
#             carbohydrate_left = self.carbohydrate_needed - self.total_carbohydrates_consumed
#             protein_left = self.protein_needed - self.total_protein_consumed
#             fat_left = self.fat_needed - self.total_fat_consumed
#
#             # Check if adding the food exceeds the needs
#             if calorie_left >= 0 and carbohydrate_left >= 0 and protein_left >= 0 and fat_left >= 0:
#                 # Add food to the all_meals dictionary with quantity
#                 # if meal not in self.all_meals:
#                 #     self.all_meals[meal] = []
#                 # self.all_meals[meal].append(f"{selected_food} ({quantity}g)")
#                 if meal not in self.all_meals:
#                     self.all_meals[meal] = []
#                 self.all_meals[meal].append((selected_food, quantity))
#
#                 self.refresh_table()
#
#                 # Show information for the added food and the remaining values
#                 messagebox.showinfo("Nutritional Information",
#                                     f"Added:\n"
#                                     f"Calories: {added_calories:.2f}\n"
#                                     f"Carbohydrates: {added_carbohydrates:.2f}\n"
#                                     f"Protein: {added_protein:.2f}\n"
#                                     f"Fat: {added_fat:.2f}\n\n"
#                                     f"Remaining:\n"
#                                     f"Calories left: {calorie_left:.2f}\n"
#                                     f"Carbohydrates left: {carbohydrate_left:.2f}\n"
#                                     f"Protein left: {protein_left:.2f}\n"
#                                     f"Fat left: {fat_left:.2f}")
#
#                 # Step 2:
#                 # # Format the foods string
#                 # formatted_foods = [f"{food} ({quantity}g)" for food in self.all_meals.get(meal, [])]
#
#                 # Step 3: Insert into MySQL table without quantity as a parameter
#                 # status, message = MealPlanController.insert_data(
#                 #     patient_id=self.patient.id,
#                 #     plan_info=self.plan_info.get(),
#                 #     calorie_needed=self.calorie_needed,
#                 #     carbohydrate_percentage=float(self.carbohydrate_percentage.get()) / 100,
#                 #     protein_percentage=float(self.protein_percentage.get()) / 100,
#                 #     fat_percentage=float(self.fat_percentage.get()) / 100,
#                 #     carbohydrate_needed=self.carbohydrate_needed,
#                 #     protein_needed=self.protein_needed,
#                 #     fat_needed=self.fat_needed,
#                 #     meal=meal,
#                 #     foods=
#                 #
#                 #     # foods=formatted_foods
#                 # )
#                 status, message = MealPlanController.insert_data(
#                     patient_id=self.patient.id,
#                     plan_info=self.plan_info.get(),
#                     calorie_needed=self.calorie_needed,
#                     carbohydrate_percentage=float(self.carbohydrate_percentage.get()) / 100,
#                     protein_percentage=float(self.protein_percentage.get()) / 100,
#                     fat_percentage=float(self.fat_percentage.get()) / 100,
#                     carbohydrate_needed=self.carbohydrate_needed,
#                     protein_needed=self.protein_needed,
#                     fat_needed=self.fat_needed,
#                     meal=meal,
#                     foods=selected_food,  # This stores the food name
#                     quantity=quantity
#                 )
#
#                 if status:
#                     messagebox.showinfo("Save Meal", "Meal plan saved successfully.")
#                 else:
#                     messagebox.showerror("Save Error", f"Failed to save meal: {message}")
#
#                 self.reset_form()
#             else:
#                 exceeded_nutrients = []
#
#                 # Check which one exceeded the needs
#                 if calorie_left < 0:
#                     exceeded_nutrients.append(f"Calories ({added_calories:.2f})")
#                 if carbohydrate_left < 0:
#                     exceeded_nutrients.append(f"Carbohydrates ({added_carbohydrates:.2f})")
#                 if protein_left < 0:
#                     exceeded_nutrients.append(f"Protein ({added_protein:.2f})")
#                 if fat_left < 0:
#                     exceeded_nutrients.append(f"Fat ({added_fat:.2f})")
#
#                 # Show a message listing the exceeded nutrients
#                 exceeded_message = ", ".join(exceeded_nutrients)
#                 # if self.carbohydrate_percentage and self.protein_percentage and self.fat_percentage:
#                 messagebox.showwarning("Nutritional Limits Exceeded",
#                                        f"Adding this food exceeds your daily "
#                                        f"nutritional goals:\n{exceeded_message}")
#                 self.reset_form()
#         else:
#             messagebox.showerror("Error", "Could not fetch nutritional values for the selected food.")
#     else:
#         messagebox.showwarning("Input Error", "Please fill in all the fields.")
#
#
#
#
#
#
#
# self.bmi_var = StringVar()
#         Label(self.window, font=("Arial Black", 14), textvariable=self.bmi_var).place(x=20, y=210)
#         # self.bmi_var.set(f"BMI : {(self.weight.get() * 10000)/self.height.get()}")