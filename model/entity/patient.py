from model.entity.user import User
from datetime import datetime
from model.validator.validation import Validation
class Patient(User):
    def __init__(self, patient_id, id, name, family, mobile, password, weight, height, age, gender):
        super().__init__(id, name, family, mobile, password)
        self.patient_id = patient_id
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.bmi = weight*10000/(height*height)
        self.date = datetime.now()


    @property
    def patient_id(self):
        return self.id

    @patient_id.setter
    def patient_id(self, patient_id):
        self.id = patient_id

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = Validation.weight_validator(weight)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = Validation.height_validator(height)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = Validation.age_validator(age)

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def bmi(self):
        return self._bmi

    @bmi.setter
    def bmi(self, bmi):
        self._bmi = bmi

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    def __repr__(self):
        return f"{self.__dict__}"



