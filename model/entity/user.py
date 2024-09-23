# from model.validator.validation import Validation
class User:
    def __init__(self, id, name, family, mobile, password, active=True):
        self.id = id
        self.name = name
        self.family = family
        self.mobile = mobile
        self.password = password


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # self._name = Validation.name_validator(name)
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        # self._family = Validation.family_validator(family)
        self._family = family

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        # self._mobile = Validation.mobile_validator(mobile)
        self._mobile = mobile

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # self._password = Validation.password_validator(password)
        self._password = password


    def __repr__(self):
        return f"{self.__dict__}"





