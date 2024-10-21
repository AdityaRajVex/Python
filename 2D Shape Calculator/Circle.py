import math


class Circle:
    def __init__(self, radius=0.0):
        # constructor
        self.___radius = radius

    def set_radius(self, r):
        self.___radius = r

    def get_radius(self):
        return self.___radius

    def cal_area(self):
        area = math.pi*self.___radius**2
        return area

    def cal_perimeter(self):
        perimeter = 2*math.pi*self.___radius
        return perimeter

    def display(self):
        print(f'The circle with radius = {self.___radius:.2f}:\n'
              f'Area = {self.cal_area():.2f}, '
              f'Perimeter = {self.cal_perimeter():.2f}')


# testing
if __name__ == '__main__':
    # circle 1, radius = 5
    c1 = Circle(5.0)
    # c1.set_radius(5.0)
    c1.display()
    print(c1)