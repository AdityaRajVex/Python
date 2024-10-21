# Name: Aditya Raj
# File Name: Date.py
# Date: 4/08/24
#
# Description: Defines the Course class
class Advisor():
    # Constructor
    def __init__(self, first_name, last_name, title, department, advisees, middle_name=None):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__title = title
        self.__department = department
        self.__advisees = advisees

    # Getters
    def getFirst_name(self):
        return self.__first_name

    def getMiddle_name(self):
        return self.__middle_name

    def getLast_name(self):
        return self.__last_name

    def getTitle(self):
        return self.__title

    def getDepartment(self):
        return self.__department

    def getAdvisees(self):
        return self.__advisees

    # Setters
    def setFirst_name(self, value):
        self.__first_name = value

    def setMiddle_name(self, value):
        self.__middle_name = value

    def setLast_name(self, value):
        self.__last_name = value

    def setTitle(self, value):
        self.__title = value

    def setDepartment(self, value):
        self.__department = value

    def setAdvisees(self, value):
        self.__advisees = value

    def execute_delete(self, value):
        if self.__advisees:
            self.__advisees.delete(value)
        else:
            print("Error: No advisee instance assigned.")
    def execute_insert(self, value):
        if self.__advisees:
            self.__advisees.insert(value)
        else:
            print("Error: No advisee instance assigned.")

    # display function
    def __str__(self):
        if self.__middle_name:
            return  (f'Name: {self.__first_name} {self.__middle_name} {self.__last_name}\n'
                     f'Title: {self.__title}\n'
                     f'Department: {self.__department}\n')
                    # f'Advisees: {self.__advisees}')

        else:
            return (f'Name: {self.__first_name} {self.__last_name}\n'
                    f'Title: {self.__title}\n'
                    f'Department: {self.__department}\n')
                    # f'Advisees: {self.getAdvisees()}')
