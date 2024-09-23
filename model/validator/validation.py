import re

class Validation:
    @classmethod
    def name_validator(self,name):
        if re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            raise ValueError("Invalid Name")

    @classmethod
    def family_validator(self, family):
        if re.match(r"^[a-zA-Z\s]{2,20}$", family):
            return family
        else:
            raise ValueError("Invalid family name")

    @classmethod
    def mobile_validator(self, mobile):
        if re.match(r"^(09|9|\+989)\d{9}$", mobile):
            return mobile
        else:
            raise ValueError("Invalid mobile number")

    @classmethod
    def password_validator(self, password):
        if re.match(r"^(?=.*[a-z]{1}.*)(?=.*\d{2})[a-zA-Z\d]{8-16}$", password):
            return password
        else:
            raise ValueError("Invalid password")
