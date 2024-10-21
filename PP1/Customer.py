class Customer():
    def __init__(self, name, age, isMember, sports):
        self.__name = name
        self.__age = age
        self.__isMember = isMember
        self.__sports = sports
        self.__fee = 0.00

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_age(self, value):
        self.__age = value

    def get_age(self):
        return self.__age

    def set_isMember(self, value):
        self.__isMember = value

    def get_isMember(self):
        return self.__isMember

    def set_sports(self, value):
        self.__sports = value

    def get_sports(self):
        return self.__sports

    def set_fee(self, value):
        self.__fee = value

    def get_fee(self):
        return self.__fee

    def add_sport(self, value):
        self.__sports.enque(value)

    def rem_sport(self):
        self.__sports.dequeue()

    def cur_sport(self):
        return self.__sports.peek()

    def calculate(self):
        if self.__age >= 60:
            fee = .9 * 50.00
            discount = .35
        elif self.__age >= 18:
            fee = 50.00
            discount = .30
        else:
            fee = 25.00
            discount = .30
        price = 0.00
        for i in self.__sports:
            price += i.get_price()
        if self.__isMember:
            price = price * (1-discount)
            price += fee
        else:
            price += fee

        self.set_fee(price)
        return price


    def __str__(self):
        return (f'Name: {self.__name}\n'
                f'Age: {self.__age}\n'
                f'Fee: ${self.__fee:.2f}\n\n')
