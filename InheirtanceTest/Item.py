# Item class, the base/super/pa
# 2/7/2024

class Item:
    def __init__(self, name='', quantity=0):
        # follow the textbook, public attributes
        self.name = name
        self.quantity = quantity

    def display(self):
        print(f'Name: {self.name}, Quantity: {self.quantity}')

    def __str__(self):
        return f'Name: {self.name}, Quantity: {self.quantity}'