from Employee import Employee


class Manager(Employee):
    def __init__(self, id, fn, ln, ann,bn):
        Employee.__init__(self, id, fn, ln)
        self.__Annual_Salary = ann
        self.__Bonus_rate = bn

    def set_salary(self, rate):
        self.__Annual_Salary = rate

    def get_AnnualSalary(self):
        return self.__Annual_Salary

    def set_bonus(self, bonus):
        self.__Bonus_rate = bonus

    def get_bonus(self):
        return self.__Bonus_rate

    def cal_monthly_pay(self):
        return self.__Annual_Salary/12 + (self.__Annual_Salary/12)*self.__Bonus_rate

    def __str__(self):
        return (Employee.__str__(self) +
                f'Annual Salary: ${self.__Annual_Salary}\n'
                f'Bonus Rate: {self.__Bonus_rate * 100}%\n'
                f'Monthly Pay: ${self.cal_monthly_pay():.2f}\n')
