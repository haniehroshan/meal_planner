import mysql.connector
from model.entity.meal_plan import MealPlan

class MealPlanDa:
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

    def insert_data(self, meal_plan):
        self.connect()
        # Convert the list of foods to a string
        foods_str = ', '.join(meal_plan.foods)
        self.cursor.execute(
            'INSERT INTO meal_plan_tbl (patient_id, date, plan_info, calorie_needed,'
            ' carbohydrate_percentage, protein_percentage, fat_percentage,'
            ' carbohydrate_needed, protein_needed, fat_needed, meal, foods, quantity) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (meal_plan.patient_id, meal_plan.date, meal_plan.plan_info, meal_plan.calorie_needed,
             meal_plan.carbohydrate_percentage, meal_plan.protein_percentage, meal_plan.fat_percentage,
             meal_plan.carbohydrate_needed, meal_plan.protein_needed, meal_plan.fat_needed,
             meal_plan.meal, foods_str, meal_plan.quantity)
        )
        self.disconnect(True)

    def edit(self, patient_id, plan_id, meal, foods, quantity):
        self.connect()
        query = '''
            UPDATE meal_plan_tbl
            SET foods = %s, quantity = %s
            WHERE patient_id = %s AND plan_id = %s AND meal = %s
            AND date = (
                SELECT date FROM meal_plan_tbl
                WHERE patient_id = %s AND plan_id = %s AND meal = %s
                ORDER BY date DESC
                LIMIT 1
            )
        '''
        self.cursor.execute(query, (foods, quantity, patient_id, plan_id, meal, patient_id, plan_id, meal))
        self.disconnect(True)

    def remove(self, patient_id, plan_id, meal):
        self.connect()
        query = '''
            DELETE FROM meal_plan_tbl
            WHERE patient_id = %s AND plan_id = %s AND meal = %s
            AND date = (
                SELECT date FROM meal_plan_tbl
                WHERE patient_id = %s AND plan_id = %s AND meal = %s
                ORDER BY date DESC
                LIMIT 1
            )
        '''
        self.cursor.execute(query, (patient_id, plan_id, meal, patient_id, plan_id, meal))
        self.disconnect(True)


    def get_all_meal_plans(self, patient_id):
        self.connect()
        self.cursor.execute('SELECT * FROM meal_plan_tbl WHERE patient_id = %s', (patient_id,))
        meal_plans = self.cursor.fetchall()
        self.disconnect()
        # convert results to MealPlan objects
        return [MealPlan(*plan) for plan in meal_plans]




