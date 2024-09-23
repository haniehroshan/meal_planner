from model.entity.user import User
from model.database.user_da import UserDa
from controller.exceptions import UserNotFoundException

class UserController:
    user_da = UserDa()

    @classmethod
    def save(cls, name, family, mobile, password):
        try:
            user = User(name, family, mobile, password)
            cls.user_da.save(user)
            return True, f"User {mobile} Saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, name, family, mobile, password):
        try:
            user = User(name, family, mobile, password)
            cls.user_da.edit(user)
            return True, f"User {mobile} Edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, mobile):
        try:
            cls.user_da.remove(mobile)
            return True, f"User {mobile} Removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, cls.user_da.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_mobile(cls, mobile):
        try:
            return True, cls.user_da.find_by_mobile(mobile)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_mobile_and_password(cls, mobile, password):
        try:
            user = cls.user_da.find_by_mobile_and_password(mobile, password)
            if user:
                return True, user
            else:
                raise UserNotFoundException("User not found !!!")
        except Exception as e:
            return False, str(e)

