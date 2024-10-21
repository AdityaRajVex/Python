#
#
#
from Date import Date
from Human import Human
class Child(Human):
    def __init__(self, name, birthday=None, school=''):
        Human.__init__(self, name, birthday)
        self.__school = school

    def display(self):
        Human.display(self)
        print(f'School: {self.__school}')