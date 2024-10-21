# Name: Aditya Raj
# File Name: Email.py
# Date: 3/31/24
#
# Description: Defines the Email class
class Email():
    # Constructor
    def __init__(self, email_address, email_type):
        self.__email_address = email_address
        self.__type = email_type

    # Getter and Setters
    def getEmailAddress(self):
        return self.__email_address

    def setEmailAddress(self, email_address):
        self.__email_address = email_address

    def getType(self):
        return self.__type

    def setType(self, email_type):
        self.__type = email_type

    # Defines the __str__ to display Email information
    def __str__(self):
        return f"{self.__email_address} ({self.__type})"
