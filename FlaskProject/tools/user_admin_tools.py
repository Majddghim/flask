from flask import session

class UserAdminTools:
    def __init__(self, connection):
        self.connection = connection

    def add_user(self, email , password, nom, prenom, tel):
        """add new user"""
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"INSERT INTO `user` (Nom , Prenom, Mail, Tel ,MDP) VALUES ('{nom}', '{prenom}', '{email}', '{tel}', '{password}')")
            self.connection.commit()
            print("User added successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
    def get_user(self, email):
        """get user by email"""
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM `user` WHERE Mail = '{email}'")
            user = cursor.fetchone()
            print(user)
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_user_session(self):
        """check if user is logged in"""
        if 'user_id' in session:
            return True
        return False