import sqlite3

class database():
    def __init__(self):
        self.connection = sqlite3.connect('API.db')
        self.cursor = self.connection.cursor()

    def selectAsNumber(self, as_number):
        self.cursor.execute(' SELECT * FROM ip2asncombined WHERE AS_number = ?', [as_number])
        return self.cursor.fetchall()

    def selectIPadd(self, ip):
        self.cursor.execute('SELECT AS_number, country_code, AS_description FROM ip2asncombined WHERE range_start = ? OR range_end = ?', [ip, ip])
        return self.cursor.fetchall()