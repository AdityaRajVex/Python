from Address import Address
from Phone import Phone


class Employee():
    def __init__(self, id, fName, lName):
        self.Company = ''
        self.__Employee_ID = id
        self.__First_Name = fName
        self.__lastName = lName
        self.__Address = Address()
        self.__PhoneList = Phone()

    def setID(self, id):
        self.__Employee_ID = id

    def getID(self):
        return self.__Employee_ID

    def setFName(self, fName):
        self.__First_Name = fName

    def getFName(self):
        return self.__First_Name

    def setLName(self, lName):
        self.__lastName = lName

    def getLName(self):
        return self.__lastName

    def setAddress(self, street, city, state, zip):
        self.__Address.setStreet(street)
        self.__Address.setCity(city)
        self.__Address.setState(state)
        self.__Address.setZipCode(zip)

    def getAddress(self):
        return self.__Address

    def setPhoneList(self, number, type):
        self.__PhoneList.setPhoneType(type)
        self.__PhoneList.setNumber(number)

    def getPhoneList(self):
        return self.__PhoneList

    def cal_Monthly_Pay(self, pr, wh):
        if pr <= 0 or wh < 0:
            raise Exception("Invalid input")
        else:
            return pr * wh

    def __str__(self):

        return (f"\n{self.__class__.__name__} Information:\n"
                f"Employee ID: {self.__Employee_ID}\n"
                f"Name: {self.__First_Name} {self.__lastName}\n"
                f"Phone Information: {self.getPhoneList()}\n"
                f"Address: {self.getAddress()}\n")


