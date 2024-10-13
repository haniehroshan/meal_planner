import mysql.connector



class PatientDa:
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

    def edit(self, weight, height, age, gender):
        self.connect()
        self.cursor.execute(
            'UPDATE patient_visit_table SET weight = %s, height = %s, age = %s, gender = %s WHERE patient_id = %s',
            (weight, height, age, gender)
        )
        self.disconnect(True)

    def remove(self, patient_id):
        self.connect()
        self.cursor.execute('DELETE FROM patient_visit_table WHERE patient_id = %s', (patient_id,))
        self.disconnect(True)

    def find_by_patient_id(self, patient_id):
        self.connect()
        self.cursor.execute(
            'SELECT * FROM patient_visit_table WHERE patient_id = %s',
            (patient_id,)
        )
        patient = self.cursor.fetchone()
        self.disconnect(True)
        return patient

    def get_patient_data(self, patient_id):
        self.connect()
        query = 'SELECT patient_id, weight, height, age, gender FROM patient_visit_table WHERE patient_id = %s'
        self.cursor.execute(query, (patient_id,))
        patient = self.cursor.fetchone()
        self.disconnect(True)
        return patient






