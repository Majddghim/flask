import pymysql

class DatabaseConnection:
    def __init__(self, host='localhost', user='root', password='', database='majdsexy'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
    def connect_to_db(self):
        """establishing connection to the database"""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connection to MySQL DB successful")
        except Exception as e:
            print(f"The error '{e}' occurred")

    def close_connection(self):
        """closing the connection to the database"""
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")
