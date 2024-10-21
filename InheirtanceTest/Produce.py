# class Produce, inherits form
# date: 02/07/24
# Developer: Aditya Raj

from Item import Item


class Produce(Item):  # inheritance declaration
    def __init__(self, name, quantity, expiration):
        Item.__init__(self, name, quantity)
        self.expiration = expiration

    def display(self):  # override
        # Item.display(self)
        print(f'name: {self.name}, Expiration: {self.expiration}')

    def __str__(self):
        return f'name: {self.name}, Expiration: {self.expiration}'


# testing
# if __name__ == '__main__':
item1 = Produce('Apple', 100, "2/1/2024")
# item1.name = 'Apple'
# item1.quantity = 100
# item1.expiration = 'Feb 20, 2024'
item1.display()
print(item1)

item2 = Item('Toy', 200)
# item2.name = 'Toy'
# item2.quantity = 200
item2.display()
print(item2)
