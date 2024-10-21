from Payroll import Payroll
# Name: Aditya Raj
# File Name: PayTester.py
# Date: 01/31/24
#
# Short Description: Test the Payroll class
# Program description output
print('This program will calculate and display the end pay for an employee')
# Initialize the data
ID = int(input("Enter employee's ID number: "))
first_name = input("Enter employee's First name: ")
last_name = input("Enter employee's Last name: ")
sales = float(input("Enter employee's sales: "))
advanced_pay = float(input("Enter employee's Advanced pay amount: "))
if advanced_pay > 2000:
    print("Advance pay can not be greater than $2000")
    exit()


# Calculations
def main():
    # testing cycle
    p = Payroll(ID=ID, first_name=first_name, last_name=last_name, sales=sales, advanced_pay=advanced_pay)
    p.display()


if __name__ == '__main__':
    main()


# Display results
'''
Testing run data
Trial 1:
    This program will calculate and display the end pay for an employee
    Enter employee's ID number: 4362334
    Enter employee's First name: Aditya
    Enter employee's Last name: Raj
    Enter employee's sales: 20000
    Enter employee's Advanced pay amount: 1100
    For Aditya Raj, id = 4362334, pay is $2100.00
    
    Process finished with exit code 0

Trial 2:
    This program will calculate and display the end pay for an employee
    Enter employee's ID number: 4362334
    Enter employee's First name: Aditya
    Enter employee's Last name: Raj
    Enter employee's sales: 123124546
    Enter employee's Advanced pay amount: 12414
    Advance pay can not be greater than $2000
    
    Process finished with exit code 0

Trial 3:
    Enter employee's ID number: 4362334
    Enter employee's First name: Aditya
    Enter employee's Last name: Raj
    Enter employee's sales: 12000
    Enter employee's Advanced pay amount: 2000
    For Aditya Raj, id = 4362334, pay is $-80.00
    
    Process finished with exit code 0
'''
