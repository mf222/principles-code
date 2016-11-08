import sqlite3


class Employee():
    def __init__(name, budget, hours):
        self.name = name
        self.budget = bud
        self.hours = hours

    def calculatePay(price):
        return self.hours*price

    def reportHours():
        return self.hours

    def increaseHours(hours):
        self.hours += hours


class StringMapper():
    def hoursToString(name, hours):
        return "{} has worked {} hours".format(name, hours)


class Database():
    conn = sqlite3.connect('database.db')

    def SaveEmployee(name, hours):
        conn.execute("INSERT INTO Employee Values(self.name, self.hours)")
