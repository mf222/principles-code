import sqlite3


class Employee():
    def __init__(self, name, budget, hours):
        self.name = name
        self.budget = bud
        self.hours = hours

    def calculatePay(self, price):
        return self.hours*price

    def reportHours(self):
        return self.hours

    def increaseHours(self, hours):
        self.hours += hours

    def hoursToString(self):
        return "{} has worked {} hours".format(self.name, self.hours)

    def save(self):
        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO Employee Values(self.name, self.hours)")
