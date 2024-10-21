# Name: Aditya Raj
# File Name: Date.py
# Date: 3/31/24
#
# Description: Defines the Date class
class Date():
    # Constructor
    def __init__(self, month, day, year):
        self.__month = month
        self.__day = day
        self.__year = year

    # Setter and Getters
    def getMonth(self):
        return self.__month

    def setMonth(self, month):
        self.__month = month

    def getDay(self):
        return self.__day

    def setDay(self, day):
        self.__day = day

    def getYear(self):
        return self.__year

    def setYear(self, year):
        self.__year = year

    # Defines the __str__ method to display Date information
    def __str__(self):
        return f'{self.__month}/{self.__day}/{self.__year}'
