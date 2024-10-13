import re

class Validation:
    @classmethod
    def name_validator(cls,name):
        if re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            raise ValueError("Invalid Name")

    @classmethod
    def family_validator(cls, family):
        if re.match(r"^[a-zA-Z\s]{2,20}$", family):
            return family
        else:
            raise ValueError("Invalid family name")

    @classmethod
    def mobile_validator(cls, mobile):
        if re.match(r"^(09|9|\+989)\d{9}$", mobile):
            return mobile
        else:
            raise ValueError("Invalid mobile number")


    @classmethod
    def password_validator(cls, password):
        # at least one lowercase letter and at least two digits, with a length between 8 and 16 characters
        if re.match(r"^(?=.*[a-z])(?=.*\d{2})[a-zA-Z\d]{8,16}$", password):
            return password
        else:
            raise ValueError("Invalid password")

    @classmethod
    def weight_validator(cls, weight):
        if 1 <= weight <= 200:
            return weight
        else:
            raise ValueError("Invalid weight")

    @classmethod
    def height_validator(cls, height):
        if 1 <= height <= 250:
            return height
        else:
            raise ValueError("Invalid height")

    @classmethod
    def age_validator(cls, age):
        if 1 <= age <= 200:
            return age
        else:
            raise ValueError("Invalid age")

    @classmethod
    def carbohydrate_percentage_validator(cls, carbohydrate_percentage):
        if 1 <= carbohydrate_percentage <= 100:
            return carbohydrate_percentage
        else:
            raise ValueError("Invalid carbohydrate_percentage")

    @classmethod
    def protein_percentage_validator(cls, protein_percentage):
        if 1 <= protein_percentage <= 100:
            return protein_percentage
        else:
            raise ValueError("Invalid protein_percentage")

    @classmethod
    def fat_percentage_validator(cls, fat_percentage):
        if 1 <= fat_percentage <= 100:
            return fat_percentage
        else:
            raise ValueError("Invalid fat_percentage")


