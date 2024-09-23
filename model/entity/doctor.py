from model.entity.user import User


class Doctor(User):
    def __init__(self, id, name, family, mobile, password, skill ):
        super().__init__(id, name, family, mobile, password)
        self.skill = skill

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, skill):
        self._skill = skill
