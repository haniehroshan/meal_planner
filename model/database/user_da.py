import mysql.connector
from model.entity.user import User


class UserDa:
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

    def save(self, name, family, mobile, password):
        self.connect()
        self.cursor.execute('INSERT INTO user_table (name, family, mobile, password)'
                            ' VALUES (%s, %s, %s, %s)', (name, family, mobile, password))
        self.disconnect(True)

    def edit(self, id, name, family, mobile, password):
        self.connect()
        self.cursor.execute(
            'UPDATE user_table SET name = %s, family = %s, mobile = %s, password = %s WHERE id = %s',
            (name, family, mobile, password, id)
        )
        self.connection.commit()
        self.disconnect(True)

    def remove(self, id):
        self.connect()
        self.cursor.execute('DELETE FROM user_table WHERE id=%s', [id])
        self.disconnect(True)

    def find_all(self):
        self.connect()
        self.cursor.execute('SELECT * FROM user_table')
        users_tuple = self.cursor.fetchall()
        if users_tuple:
            user_list = []
            for user in users_tuple:
                user_list.append(User(*user))
            self.disconnect()
            return user_list

    def find_by_mobile(self, mobile):
        self.connect()
        self.cursor.execute('SELECT * FROM user_table WHERE mobile=%s', [mobile])
        user_tuple = self.cursor.fetchone()
        user = User(*user_tuple)
        self.disconnect()
        return user

    def find_by_name_and_family(self, name, family):
        self.connect()
        self.cursor.execute('SELECT * FROM user_table WHERE name=%s AND family=%s', [name, family])
        user_tuple = self.cursor.fetchone()
        user = User(*user_tuple)
        self.disconnect()
        return user

    def find_by_mobile_and_password(self, mobile, password):
        self.connect()
        self.cursor.execute('SELECT * FROM user_table WHERE mobile=%s AND password=%s', [mobile, password])
        user_tuple = self.cursor.fetchone()
        user = User(*user_tuple)
        self.disconnect()
        return user

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute('SELECT * FROM user_table WHERE id=%s', [id])
        user_tuple = self.cursor.fetchone()
        user = User(*user_tuple)
        self.disconnect()
        return user
