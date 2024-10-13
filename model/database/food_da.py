# خواندن اطلاعات از
# یک دیتابیسی که به شکل فایل اکسلcsvبوده و به Mysql ایمپورت شده
import mysql.connector
class FoodDa:
    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root123',
            database='planner'
        )
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

# todo:
    # for options in Combobox food_name search
    def find_by_food_name(self, food_name):
        self.connect()
        if food_name:  # If food_name is provided
            self.cursor.execute('SELECT * FROM food_composition_tbl WHERE food_name LIKE %s',
                                ('%' + food_name + '%',))
        else:  # If food_name is empty, return all
            self.cursor.execute('SELECT * FROM food_composition_tbl')
        options = self.cursor.fetchall()
        self.disconnect()
        print("Fetched options:", options)  # Debug print to check fetched results
        return options

    def load_food_items(self):
        """Fetch all food items from the database and populate the Combobox."""
        self.connect()
        self.cursor.execute('SELECT food_name FROM food_composition_tbl')
        food_options = self.cursor.fetchall()
        self.disconnect()
        return food_options

    # def fetch_nutritional_values(self, food_name):
    #     self.connect()
    #     if food_name:
    #         self.cursor.execute('SELECT food_amount, food_calorie, food_carbohydrate, food_protein, food_fat FROM food_composition_tbl WHERE food_name = %s', (food_name,))
    #     nutritional_values = self.cursor.fetchone()
    #     self.disconnect()
    #     return nutritional_values

    def fetch_nutritional_values(self, food_name):
        self.connect()
        if food_name:
            self.cursor.execute(
                'SELECT food_amount, food_calorie, food_carbohydrate, food_protein, food_fat '
                'FROM food_composition_tbl WHERE food_name = %s',
                (food_name,)
            )
            nutritional_values = self.cursor.fetchone()
            self.disconnect()

            # Check if the nutritional_values is not None and has the expected number of elements
            if nutritional_values and len(nutritional_values) == 5:
                return nutritional_values
            else:
                return None  # Return None if not enough values are found






