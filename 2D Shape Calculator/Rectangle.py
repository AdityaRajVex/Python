#
#
#
class Rectangle:
    def __init__(self, length = 0.0, width = 0.0):
        #length, width
        self.__length = length
        self.__width = width

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_width(self, width):
        self.__width = width

    def get_width(self ):
        return self.__width

    def cal_area(self):
        return self.__width * self.__length

    def cal_perimeter(self ):
        return (self.__width + self.__length) * 2.0

    def __str__(self):
        return f'The rectangle with length = {self.__length:.2f}, width = {self.__width:.2f}: \n Area = {self.cal_area():.2f}, Perimeter = {self.cal_perimeter()}'


# inner module testing
if __name__ == '__main__':
    rect1 = Rectangle(10.6, 3.6)
    print(rect1)
