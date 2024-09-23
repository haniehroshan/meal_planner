import mysql.connector
from model.entity.patient import Patient
from model.database.user_da import UserDa


class PatientDa(UserDa):
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

    def save(self, patient_id, weight, height, age, gender):
        self.connect()
        self.cursor.execute(
            'INSERT INTO patient_visit_table (patient_id, weight, height, age, gender, date) VALUES (%s, %s, %s, %s, %s, %s)',
            (patient_id, weight, height, age, gender)
        )
        self.disconnect(True)

    def edit(self, patient_id, weight, height, age, gender):
        self.connect()
        self.cursor.execute(
            'UPDATE patient_visit_table SET weight = %s, height = %s, age = %s, gender = %s WHERE patient_id = %s',
            (weight, height, age, gender)
        )
        self.disconnect(True)




