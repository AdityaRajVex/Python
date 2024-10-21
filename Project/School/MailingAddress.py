# Name: Aditya Raj
# File Name: MailingAddress.py
# Date: 3/31/24
#
# Description: defines the MailingAddress class
class MailingAddress():
    # Constructor
    def __init__(self, street, city, state, zip_code, type):
        self.__Street = street
        self.__City = city
        self.__State = state
        self.__zipCode = zip_code
        self.__type = type

    # Setter and Getters
    def setStreet(self, streetNo):
        self.__Street = streetNo

    def getStreet(self):
        return self.__Street

    def setCity(self, city):
        self.__City = city

    def getCity(self):
        return self.__City

    def setState(self, state):
        self.__State = state

    def getState(self):
        return self.__State

    def setZipCode(self, zipCode):
        self.__zipCode = zipCode

    def getZipCode(self):
        return self.__zipCode

    def setType(self, residence_type):
        self.__type = residence_type

    def getType(self):
        return self.__type

    # Defines the __str__ method to display the MailingAddress info
    def __str__(self):
        return f"{self.__Street}, {self.__City}, {self.__State} {self.__zipCode} ({self.__type})"

