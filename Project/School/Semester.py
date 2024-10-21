# Name: Aditya Raj
# File Name: Semester.py
# Date: 3/31/24
#
# Description: Defines the Semester class
class Semester():
    # Constructor
    def __init__(self, semester, year):
        self.__semester = semester
        self.__year = year

    # Setter and Getters
    def getSemester(self):
        return self.__semester

    def setSemester(self, semester):
        self.__semester = semester

    def getYear(self):
        return self.__year

    def setYear(self, year):
        self.__year = year

    # defines the __str__ method to display Semester information
    def __str__(self):
        return f"{self.__semester} {self.__year}"
