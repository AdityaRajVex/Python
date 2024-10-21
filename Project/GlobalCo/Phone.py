class Phone():
    def __init__(self):
        self.__Phone_No = ''
        self.__Phone_Type = ''

    def setNumber(self, number):
        self.__Phone_No = number

    def getNumber(self):
        return self.__Phone_No

    def setPhoneType(self, phoneType):
        self.__Phone_Type = phoneType

    def getPhoneType(self):
        return self.__Phone_Type

    def __str__(self):
        return f'{self.__Phone_No} ({self.__Phone_Type})'


