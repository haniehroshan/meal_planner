

class select_food:
    def __init__(self, patient_id, food_name, food_amount):
        self.patient_id = patient_id
        self.food_name = food_name
        self.food_amount = food_amount

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
    def food_amount(self, value):
        self._food_amount = value