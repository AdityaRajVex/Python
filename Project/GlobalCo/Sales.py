from Employee import Employee

class Sales(Employee):
    def __init__(self, id, fn, ln, sales, comm):
        Employee.__init__(self, id, fn, ln)
        self.__sales = sales
        self.__commission_rate = comm

    def setRate(self, rate):
        self.__commission_rate = rate

    def getRate(self):
        return self.__commission_rate

    def set_sales(self, sales):
        self.__sales = sales

    def get_sales(self):
        return self.__sales

    def cal_monthly_pay(self):
        return self.__sales * self.__commission_rate

    def __str__(self):
        return Employee.__str__(self) + (f'\n'
                                         f'Sales: ${self.__sales}\n'
                                         f'Commission Rate: {self.__commission_rate * 100}%\n'
                                         f'Monthly Pay: ${self.cal_monthly_pay():.2f}')

