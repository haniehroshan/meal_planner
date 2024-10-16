from model.database.meal_plan_da import MealPlanDa
from model.entity.meal_plan import MealPlan


class MealPlanController:
    meal_plan_da = MealPlanDa()

    @classmethod
    def insert_data(cls, patient_id, plan_info, calorie_needed, carbohydrate_percentage,
                    protein_percentage, fat_percentage, carbohydrate_needed,
                    protein_needed, fat_needed, meal, foods, quantity):
        try:
            # Create a MealPlan object (date is not needed here as it's auto-generated)
            meal_plan = MealPlan(patient_id=patient_id, plan_info=plan_info, plan_id=None,
                                 calorie_needed=calorie_needed, carbohydrate_percentage=carbohydrate_percentage,
                                 protein_percentage=protein_percentage, fat_percentage=fat_percentage,
                                 carbohydrate_needed=carbohydrate_needed, protein_needed=protein_needed,
                                 fat_needed=fat_needed, meal=meal, foods=foods, quantity=quantity)

            # Insert the meal plan data into the database
            cls.meal_plan_da.insert_data(meal_plan)
            return True, f"Meal plan for {patient_id} saved."
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, patient_id, plan_id, meal, foods, quantity):
        try:
            # Update the meal plan data in the database
            cls.meal_plan_da.edit(
                patient_id=patient_id,
                plan_id=plan_id,
                meal=meal,
                foods=foods,
                quantity=quantity
            )
            return True, "Meal plan updated."
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, patient_id, plan_id, meal, foods):
        try:
            # Delete the meal plan from the database
            cls.meal_plan_da.remove(patient_id=patient_id, plan_id=plan_id, meal=meal, foods=foods)
            return True, "Meal plan removed."
        except Exception as e:
            return False, str(e)

    @classmethod
    def get_all_meal_plans(cls, patient_id):
        return cls.meal_plan_da.get_all_meal_plans(patient_id)  # Fetch all plans for the patient
