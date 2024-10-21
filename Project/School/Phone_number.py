# Name: Aditya Raj
# File Name: Phone_number.py
# Date: 3/31/24
#
# Description: Defines the Phone_number class
class Phone_number():
    # Constructor
    def __init__(self, phone_no, type):
        self.__Phone_No = phone_no
        self.__Phone_Type = type

    # Setter and Getters
    def setNumber(self, number):
        self.__Phone_No = number

    def getNumber(self):
        return self.__Phone_No

    def setPhoneType(self, phoneType):
        self.__Phone_Type = phoneType

    def getPhoneType(self):
        return self.__Phone_Type

    # Defines the __str__ method to display Phone_number information
    def __str__(self):
        return f"{self.__Phone_No} ({self.__Phone_Type})"


