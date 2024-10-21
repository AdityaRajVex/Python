# abstract class for general human
# for inheritance

from Date import Date


class Human:
    def __init__(self, name, dob=None):
        self.__name = name
        self.__birthday = dob

    def display(self):
        print(f'Name:{self.__name}')
        print('Birthday: ', end='')
        self.__birthday.display()

    def __str__(self):
        return f'Name: {self.__name}, Birthday: {self.__birthday}'

