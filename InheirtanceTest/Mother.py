#
#
#
from Human import Human
from Child import Child
from Date import Date

class Mother(Human):
    def __init__(self, name, dob=None, children=[]):
        Human.__init__(self, name, dob)
        self.__children = children

    def display(self):
        Human.display(self)
        print('Children: ')
        for e in self.__children:
            #print(e)
            e.display()

if __name__ == '__main__':
    name = input('Enter the mother name: ')
    month = int(input('Enter the birthday month: '))
    day = int(input('Enter the birthday day: '))
    year = int(input('Enter the birthday year: '))
    dob = Date(month, day, year)
    children = []
    flag = 1
    while flag:
        child_name = input('Enter the child name: ')
        m = int(input('Enter the birthday month: '))
        d = int(input('Enter the birthday day: '))
        y = int(input('Enter the birthday year: '))
        child_dob = Date(m, d, y)
        school = input('Enter school name: ')
        child1 = Child(child_name, child_dob, school)
        children.append(child1)
        flag = int(input('Add another child? Enter 1 for yes and 0 for no'))

    mom1 = Mother(name, dob, children)
    mom1.display()