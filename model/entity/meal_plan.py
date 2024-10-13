
from datetime import datetime


class MealPlan:
    def __init__(self, patient_id, plan_info, plan_id, calorie_needed, carbohydrate_percentage,
                 protein_percentage, fat_percentage, carbohydrate_needed,
                 protein_needed, fat_needed, meal, foods, quantity):

        self.patient_id = patient_id
        self.date = datetime.now()
        self.plan_info = plan_info
        self.plan_id = plan_id
        self.calorie_needed = calorie_needed
        self.carbohydrate_percentage = carbohydrate_percentage
        self.protein_percentage = protein_percentage
        self.fat_percentage = fat_percentage
        self.carbohydrate_needed = carbohydrate_needed
        self.protein_needed = protein_needed
        self.fat_needed = fat_needed
        self.meal = meal
        self.foods = foods
        self.quantity = quantity




    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        self._patient_id = patient_id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def plan_info(self):
        return self._plan_info

    @plan_info.setter
    def plan_info(self, plan_info):
        self._plan_info = plan_info

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        self._plan_id = plan_id

    @property
    def calorie_needed(self):
        return self._calorie_needed

    @calorie_needed.setter
    def calorie_needed(self, calorie_needed):
        self._calorie_needed = calorie_needed

    @property
    def carbohydrate_percentage(self):
        return self._carbohydrate_percentage

    @carbohydrate_percentage.setter
    def carbohydrate_percentage(self, carbohydrate_percentage):
        self._carbohydrate_percentage = carbohydrate_percentage

    @property
    def protein_percentage(self):
        return self._protein_percentage

    @protein_percentage.setter
    def protein_percentage(self, protein_percentage):
        self._protein_percentage = protein_percentage

    @property
    def fat_percentage(self):
        return self._fat_percentage

    @fat_percentage.setter
    def fat_percentage(self, fat_percentage):
        self._fat_percentage = fat_percentage


    @property
    def carbohydrate_needed(self):
        return self._calorie_needed

    @carbohydrate_needed.setter
    def carbohydrate_needed(self, carbohydrate_needed):
        self._carbohydrate_needed = carbohydrate_needed

    @property
    def protein_needed(self):
        return self._protein_needed

    @protein_needed.setter
    def protein_needed(self, protein_needed):
        self._protein_needed = protein_needed

    @property
    def fat_needed(self):
        return self._fat_needed

    @fat_needed.setter
    def fat_needed(self, fat_needed):
        self._fat_needed = fat_needed

    @property
    def meal(self):
        return self._meal

    @meal.setter
    def meal(self, meal):
        self._meal = meal

    @property
    def foods(self):
        return self._foods

    @foods.setter
    def foods(self, foods):
        self._foods = foods

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity


    def __repr__(self):
        return f"{self.__dict__}"
