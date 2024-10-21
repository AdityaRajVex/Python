class Inventory():
    def __init__(self, num, lotNum):
        self.__num = num
        self.__lotNum = lotNum

    def get_lotnum(self):
        return self.__lotNum

    def __str__(self):
        return f'{self.__num}'

    def __eq__(self, other):
        if self.__num == other.get_num():
            return True
        else:
            return False

    def __le__(self, other):
        if self.__num <= other.get_num()
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__num < other.ge_num()
            return True
        else:
            return False
