from Circle import Circle
from Rectangle import Rectangle

def main():
    isTrue = 1
    while isTrue:
        # testing circle
        radius = float(input('Enter a value for radius: '))
        if radius > 0:
            c = Circle(radius)
            print(c)

        # testing rectangle
        l, w = float(input('Enter value for length and width: '))
        if l >= 0 and w >= 0:
            rect = Rectangle(l, w)
            print(rect)

        isTrue = int(input('Continue to test? Enter 1 for yes, 0 for no'))
    print('Well done! byebye')

if __name__ == '__main__':
    main()