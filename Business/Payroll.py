class Payroll:
    def __init__(self, ID, first_name, last_name, sales, advanced_pay):
        self.__id = ID
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sales = sales
        self.__advanced_pay = advanced_pay

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_sales(self):
        return self.__sales

    def set_sales(self, sales):
        self.__sales = sales

    def get_advanced_pay(self):
        return self.__advanced_pay

    def set_advanced_pay(self, advanced_pay):
        self.__advanced_pay = advanced_pay

    def calcPay(self):
        if self.__sales < 10000:
            commission = 0.10
        if self.__sales < 15000:
            commission = 0.12
        if self.__sales < 18000:
            commission = 0.14
        if self.__sales < 22000:
            commission = 0.16
        else:
            commission = self.__sales * 0.18
        pay = self.__sales * commission - self.__advanced_pay
        return pay

    def display(self):
        print(f'For {self.__first_name} {self.__last_name}, id = {self.__id}, pay is ${self.calcPay():.2f}')
