from model.entity.user import User
from datetime import datetime

from model.entity.user import User
from datetime import datetime

class Patient(User):
    def __init__(self, patient_id, id, name, family, mobile, password, weight, height, age, gender):
        super().__init__(id, name, family, mobile, password)
        self.patient_id = patient_id
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.date = datetime.today()

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def patient_id(self):
        return self.id

    @patient_id.setter
    def patient_id(self, patient_id):
        self.id = patient_id
