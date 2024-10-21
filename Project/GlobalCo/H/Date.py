# manage date by mm/dd/yyyy
# 2/12/2024

class Date:
    def __init__(self, mm=1, dd=1, year=2020):
        self.__month = mm
        self.__day = dd
        self.__year = year

    def set_month(self, month):
        self.__month = month

    def set_day(self, day):
        self.__day = day

    def set_year(self, year):
        self.__year = year

    # Getters are skipped

    def display(self):
        print(f'{self.__month}/{self.__day}/{self.__year}')

    def __str__(self):
        return f'{self.__month}/{self.__day}/{self.__year}'