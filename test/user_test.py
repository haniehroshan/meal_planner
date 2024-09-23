from controller.user_controller import UserController
from model.entity.user import User
from model.database.user_da import UserDa


user_da = UserDa()
# user_da.save("Payman", "Roshan", "09122110871", "pr09122110871")
# user_da.save("Majid", "Roshan", "09121467477", "mr09121467477")
# user_da.save("Hanieh", "Roshan", "09128363114", "hr09128363114")
# user_da.remove("09128363114")
# user_da.save("Hanieh", "Roshan", "09128363114", "hr09128363114")
# user_da.save("Mahshid", "Talayi", "09361367042", "mt09361367042")
# user_da.edit(3, "payman", "roshan", "09122110871", "pr09122110871")
print(UserController.find_by_mobile_and_password("09122110871", "pr09122110871"))
