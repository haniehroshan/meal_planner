
from model.database.food_da import FoodDa
from controller.exceptions import FoodNotFoundException


class FoodController:
    food_da = FoodDa()

    @classmethod
    def find_by_food_name(cls, food_name):
        try:
            option = cls.food_da.find_by_food_name(food_name)
            if option:
                return True, option
            else:
                raise FoodNotFoundException("Food not found!")
        except Exception as e:
            return False, str(e)

    # @classmethod
    # def fetch_nutritional_values(cls, food_name):
    #     try:
    #         nutritional_values = cls.food_da.fetch_nutritional_values(food_name)
    #         if nutritional_values:
    #             return nutritional_values
    #         else:
    #             raise FoodNotFoundException("Food not found!")
    #     except Exception as e:
    #         return False, str(e)
    @classmethod
    def fetch_nutritional_values(cls, food_name):
        try:
            nutritional_values = cls.food_da.fetch_nutritional_values(food_name)
            if nutritional_values:
                return nutritional_values  # This should be a tuple of 5 values
            else:
                raise FoodNotFoundException("Food not found!")
        except Exception as e:
            return None

    @classmethod
    def load_food_items(cls):
        try:
            food_options = cls.food_da.load_food_items()
            if food_options:
                return food_options
            else:
                raise FoodNotFoundException("Food not found!")
        except Exception as e:
            return False, str(e)







