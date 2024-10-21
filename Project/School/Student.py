# Name: Aditya Raj
# File Name: Email.py
# Date: 3/31/24
#
# Description: Defines the Student class

from LinkedList import LinkedList
class Student():
    # constructor
    def __init__(self, name, id, mailing_address, email, phone_number, birth_date, acceptance_date, semester_start, intended_major, course_list):
        self.__name = name
        self.__id = id
        self.__mailing_address = mailing_address
        self.__email = email
        self.__phone_number = phone_number
        self.__birth_date = birth_date
        self.__acceptance_date = acceptance_date
        self.__semester_start = semester_start
        self.__intended_major = intended_major
        self.__course_list = course_list

    # Setter and Getters
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    def getMailingAddress(self):
        return self.__mailing_address

    def getCourses(self):
        return self.__course_list

    def setCourses(self, Courses):
        self.__course_list = Courses

    def setMailingAddress(self, mailing_address):
        self.__mailing_address = mailing_address

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPhoneNumber(self):
        return self.__phone_number

    def setPhoneNumber(self, phone_number):
        self.__phone_number = phone_number

    def getBirthDate(self):
        return self.__birth_date

    def setBirthDate(self, birth_date):
        self.__birth_date = birth_date

    def getAcceptanceDate(self):
        return self.__acceptance_date

    def setAcceptanceDate(self, acceptance_date):
        self.__acceptance_date = acceptance_date

    def getSemesterStart(self):
        return self.__semester_start

    def setSemesterStart(self, semester_start):
        self.__semester_start = semester_start

    def getIntendedMajor(self):
        return self.__intended_major

    def setIntendedMajor(self, intended_major):
        self.__intended_major = intended_major

    # Function to display class attributes that are lists
    def displayList(self, list):
        list_string = ""
        if not list:
            list_string = "Not Set\n"
        else:
            for i in list:
                list_string += f"{i.__str__()}\n"
        return list_string

    # Defines the __str__ method to display Student information
    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'ID: {self.__id}\n'
                f'Mailing Address: {self.__mailing_address.__str__()}\n'
                f'Email: {self.displayList(self.__email)}\n'
                f'Phone: {self.displayList(self.__phone_number)}\n'
                f'Birth Date: {self.__birth_date.__str__()}\n'
                f'Acceptance Date: {self.__acceptance_date.__str__()}\n'
                f'Semester Start: {self.__semester_start.__str__()}\n'
                f'Intended Major: {self.__intended_major.__str__()}')
