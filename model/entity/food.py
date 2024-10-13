# These come from CSV file in database not by the user
class Food:
    def __init__(self, food_name, food_amount, food_calorie, food_carbohydrate, food_protein,
                 food_fat):
        self.food_name = food_name
        self.food_amount = food_amount
        self.food_calorie = food_calorie
        self.food_carbohydrate = food_carbohydrate
        self.food_protein = food_protein
        self.food_fat = food_fat


    @property
    def food_name(self):
        return self._food_name

    @food_name.setter
    def food_name(self, food_name):
        self._food_name = food_name


    @property
    def food_amount(self):
        return self._food_amount

    @food_amount.setter
    def food_amount(self, food_amount):
        self._food_amount = food_amount

    @property
    def food_calorie(self):
        return self._food_calorie

    @food_calorie.setter
    def food_calorie(self, food_calorie):
        self._food_calorie = food_calorie

    @property
    def food_carbohydrate(self):
        return self._food_carbohydrate

    @food_carbohydrate.setter
    def food_carbohydrate(self, food_carbohydrate):
        self._food_carbohydrate = food_carbohydrate

    @property
    def food_protein(self):
        return self._food_protein

    @food_protein.setter
    def food_protein(self, food_protein):
        self._food_protein = food_protein

    @property
    def food_fat(self):
        return self._food_fat

    @food_fat.setter
    def food_fat(self, food_fat):
        self._food_fat = food_fat

    def __repr__(self):
        return f"{self.__dict__}"

   




