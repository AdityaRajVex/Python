class Procedure:
    def __init__(self, name, date, practitioner, charges):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_practitioner(self):
        return self.__practitioner

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def get_charges(self):
        return self.__charges

    def set_charges(self, charges):
        self.__charges = charges
