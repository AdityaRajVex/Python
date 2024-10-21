#
#
#
from Stock import Stock


class Transaction(Stock):
    def __init__(self, stock=Stock, types='Sell', trade_price=0.0, quantity=0):
        Stock.__init__(self, stock)
        self.__type = types
        self.__trade_price = trade_price
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def __str__(self):
        return (f'Stock Name: {Stock.get_name(self)}\n'
                f'Trade Type: {self.__type}\n'
                f'Trade Price: {self.__trade_price}\n'
                f'Quantity: {self.__quantity}')

