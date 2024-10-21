#
#
#
class Stock:
    def __init__(self, name='', sell_price=0.0, buy_price=0.0):
        self.__name = name
        self.__sell_price = sell_price
        self.__buy_price = buy_price

    # getters
    def get_name(self):
        return self.__name

    def get_sell_price(self):
        return self.__sell_price

    def get_buy_price(self):
        return self.__buy_price
