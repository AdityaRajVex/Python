class Address():
    def __init__(self):
        self.__Street = ''
        self.__City = ''
        self.__State = ''
        self.__zipCode = ''

    def setStreet(self, streetNo):
        self.__Street = streetNo

    def getStreet(self):
        return self.__Street

    def setCity(self, city):
        self.__City = city

    def getCity(self):
        return self.__City

    def setState(self, state):
        self.__State = state

    def getState(self):
        return self.__State

    def setZipCode(self, zipCode):
        self.__zipCode = zipCode

    def getZipCode(self):
        return self.__zipCode

    def __str__(self):
        return f'{self.__Street}, {self.__City}, {self.__State} {self.__zipCode}'

