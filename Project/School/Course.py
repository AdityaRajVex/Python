# Name: Aditya Raj
# File Name: Date.py
# Date: 4/08/24
#
# Description: Defines the Course class
class Course():
    # Constructor
    def __init__(self, course_name, semester_taken, style, status, grade):
        self.__course_name = course_name
        self.__semester_taken = semester_taken
        self.__style = style
        self.__status = status
        self.__grade = grade

    # Getters
    def getCourse_name(self):
        return self.__course_name

    def getSemester_taken(self):
        return self.__semester_taken

    def getStyle(self):
        return self.__style

    def getStatus(self):
        return self.__status

    def getGrade(self):
        return self.__grade

    # Setters
    def setCourse_name(self, value):
        self.__course_name = value

    def setSemester_taken(self, value):
        self.__semester_taken = value

    def setStyle(self, value):
        self.__style = value

    def setStatus(self, value):
        self.__status = value

    def setGrade(self, value):
        self.__grade = value

    def execute_delete(self, value):
        if self.c:
            self.__advisees.delete(value)
        else:
            print("Error: No advisee instance assigned.")
    def execute_insert(self, value):
        if self.__advisees:
            self.__advisees.insert(value)
        else:
            print("Error: No advisee instance assigned.")

    # displays the attributes
    def __str__(self):
        return (f'Course: {self.__course_name} Semester: {self.__semester_taken}\n'
                f'Style: {self.__style} Status: {self.__status} Grade: {self.__grade}')
