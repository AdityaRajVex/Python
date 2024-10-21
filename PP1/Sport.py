class Sport():
    def __init__(self, name, series_num, price=0.0):
        self.__name = name
        self.__series_num = series_num
        self.__price = price

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_series_num(self, value):
        self.__series_num = value

    def get_series_num(self):
        return self.__series_num

    def set_price(self, value):
        self.__price = value

    def get_price(self):
        return self.__price

    def __str__(self):
        return (f'Name: {self.__name}'
                f'series_num: {self.__series_num}'
                f'Price: {self.__price}')

