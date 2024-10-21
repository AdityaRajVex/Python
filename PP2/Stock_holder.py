#
#
#
from Transaction import Transaction
from Stock import Stock


class StockHolder:
    def __init__(self, user_name='', balance=0.0, stocks={}, transactions=[]):
        self.__user_name = user_name
        self.__balance = balance
        self.__stocks = stocks
        self.__transactions = transactions

    # setters
    def deposit(self, amount=0.0):
        self.__balance = amount

    # getters
    def get_name(self):
        return self.__user_name

    def get_balance(self):
        return self.__balance

    def buy(self, stock, set_price, quantity):
        if set_price < Transaction.get_buy_price(stock):
            print('A transaction could not be made')
        elif self.__balance < set_price:
            print('A transaction could not be made')
        else:
            t1 = Transaction(stock, 'Buy', set_price, quantity)
            self.__transactions.append(t1)
            self.__balance = self.get_balance() - set_price*quantity

    def sell(self, stock, set_price, quantity):
        if set_price > Transaction.get_sell_price(stock) or quantity > Transaction.get_quantity(stock):
            print('A transaction could not be made')
        else:
            t2 = Transaction(stock, 'Sell', set_price, quantity)
            self.__transactions.append(t2)
            self.__balance = self.get_balance() + set_price*quantity

    def display(self):
        return (f'User Name: {self.__user_name}\n'
                f'Stocks: {self.__stocks}\n'
                f'Transactions: {self.__transactions}')


if __name__ == '__main__':
    TSLA = Stock('TSLA', 199, 200)
    APPL = Stock('APPL', 140, 145)
    GOOGL = Stock('GOOGL', 148, 150)
    NVDA = Stock('NVDA', 850, 800)
    QQQ = Stock('QQQ', 445, 432)

    username = input('Enter user name: ')
    balances = float(input('Enter user balance: '))

    Sh = StockHolder(username, balances)
    print(f'Trade Holder: {Sh.get_name()}\n'
          f'Balance: {Sh.get_balance()}')
