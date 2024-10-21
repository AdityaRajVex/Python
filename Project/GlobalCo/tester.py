# Name: Aditya Raj
# File Name: tester.py
# Date: 02/23/24
#
# Short Description: Test the manager and sales classes
# Program description output
print('This program will test the manager and sale classes and display the output')

# Initialize the data
from Sales import Sales
from Manager import Manager
# Calculations


def main():
    # Initialize a variable to control the loop
    isTrue = 1
    while isTrue:
        # Prompt the user to choose between Manager ('M') or Sales ('S') options, or to quit ('Q')
        choice = input("Enter 'M' for Manager or 'S' for Sales (Q to quit): ").upper()
        if choice == 'M':
            # If Manager option is chosen, gather information about the manager
            id = int(input('Enter the ID: '))
            fn = input('Enter the First Name: ')
            ln = input('Enter the Last Name: ')
            ann = int(input('Enter the Annual Salary: '))
            bn = float(input('Enter the Bonus Rate: '))
            # Create a Manager object with the provided information
            m = Manager(id, fn, ln, ann, bn)
            # Check if the user wants to add phone information
            cphone = input('Enter Phone information? Y for yes and N for no: ').upper()
            if cphone == 'Y':
                pn = input('Enter Phone number: ')
                pt = input('Enter Phone type: ')
                m.setPhoneList(pn, pt)
            else:
                m.setPhoneList('N/A', 'N/A')
            # Check if the user wants to add address information
            caddress = input('Enter Address information? Y for yes and N for no: ').upper()
            if caddress == 'Y':
                st = input('Enter Street name: ')
                ct = input('Enter City name: ')
                se = input('Enter State name: ')
                zc = input('Enter Zip code: ')
                m.setAddress(st, ct, se, zc)
            else:
                m.setAddress('N/A', 'N/A', 'N/A', 'N/A')
            # Display the manager's information and calculate monthly pay
            print(m)
            m.cal_monthly_pay()
        elif choice == 'S':
            # If Sales option is chosen, gather information about the salesperson
            id = int(input('Enter the ID: '))
            fn = input('Enter the First Name: ')
            ln = input('Enter the Last Name: ')
            sales = float(input('Enter the Sales: '))
            comm = float(input('Enter the Commission Rate: '))
            # Create a Sales object with the provided information
            s = Sales(id, fn, ln, sales, comm)
            # Check if the user wants to add phone information
            cphone = input('Enter Phone information? Y for yes and N for no: ').upper()
            if cphone == 'Y':
                pn = input('Enter Phone number: ')
                pt = input('Enter Phone type: ')
                s.setPhoneList(pn, pt)
            else:
                s.setPhoneList('N/A', 'N/A')
            # Check if the user wants to add address information
            caddress = input('Enter Address information? Y for yes and N for no: ').upper()
            if caddress == 'Y':
                st = input('Enter Street name: ')
                ct = input('Enter City name: ')
                se = input('Enter State name: ')
                zc = input('Enter Zip code: ')
                s.setAddress(st, ct, se, zc)
            else:
                s.setAddress('N/A', 'N/A', 'N/A', 'N/A')
            # Display the salesperson's information and calculate monthly pay
            print(s)
            s.cal_monthly_pay()
        elif choice == 'Q':
            # If Quit option is chosen, exit the loop
            isTrue = 0
        else:
            # If an invalid option is chosen, prompt the user to choose again
            print("Invalid choice. Please enter 'M' for Manager, 'S' for Sales, or 'Q' to quit.")


if __name__ == '__main__':
    main()
# Display results
'''
testing run data:
Trial 1:
    This program will test the manager and sale classes and display the output
    Enter 'M' for Manager or 'S' for Sales (Q to quit): M
    Enter the ID: 12345
    Enter the First Name: Aditya
    Enter the Last Name: Raj
    Enter the Annual Salary: 130000
    Enter the Bonus Rate: .12
    Enter Phone information? Y for yes and N for no: y
    Enter Phone number: (610)710-9692
    Enter Phone type: Iphone
    Enter Address information? Y for yes and N for no: Y
    Enter Street name: 25 Yearsly Mill Rd
    Enter City name: Media
    Enter State name: PA
    Enter Zip code: 19063
    Manager Information:
    Employee ID: 12345
    Name: Aditya Raj
    Phone Information: (610)710-9692 (Iphone)
    Address: 25 Yearsly Mill Rd, Media, PA 19063
    Annual Salary: $130000
    Bonus Rate: 12.0%
    Monthly Pay: $12133.33
    
    Enter 'M' for Manager or 'S' for Sales (Q to quit): S
    Enter the ID: 12345
    Enter the First Name: Matt
    Enter the Last Name: Yu
    Enter the Sales: 5000
    Enter the Commission Rate: .1
    Enter Phone information? Y for yes and N for no: y
    Enter Phone number: (267)541-4970
    Enter Phone type: Iphone
    Enter Address information? Y for yes and N for no: y
    Enter Street name: 525 Radek Ct
    Enter City name: West Chester
    Enter State name: PA
    Enter Zip code: 19382
    Sales Information:
    Employee ID: 12345
    Name: Matt Yu
    Phone Information: (267)541-4970 (Iphone)
    Address: 525 Radek Ct, West Chester, PA 19382
    
    Sales: $5000.0
    Commission Rate: 10.0%
    Monthly Pay: $500.00
    Enter 'M' for Manager or 'S' for Sales (Q to quit): q

    Process finished with exit code 0

Trial 2:
    This program will test the manager and sale classes and display the output
    Enter 'M' for Manager or 'S' for Sales (Q to quit): M
    Enter the ID: 123456
    Enter the First Name: Aditya
    Enter the Last Name: Raj
    Enter the Annual Salary: 1231321
    Enter the Bonus Rate: .1
    Enter Phone information? Y for yes and N for no: n
    Enter Address information? Y for yes and N for no: n
    
    Manager Information:
    Employee ID: 123456
    Name: Aditya Raj
    Phone Information: N/A (N/A)
    Address: N/A, N/A, N/A N/A
    Annual Salary: $1231321
    Bonus Rate: 10.0%
    Monthly Pay: $112871.09
    
    Enter 'M' for Manager or 'S' for Sales (Q to quit): s
    Enter the ID: 12345
    Enter the First Name: Matt
    Enter the Last Name: Yu
    Enter the Sales: 12312
    Enter the Commission Rate: .2
    Enter Phone information? Y for yes and N for no: n
    Enter Address information? Y for yes and N for no: n
    
    Sales Information:
    Employee ID: 12345
    Name: Matt Yu
    Phone Information: N/A (N/A)
    Address: N/A, N/A, N/A N/A
    
    Sales: $12312.0
    Commission Rate: 20.0%
    Monthly Pay: $2462.40
    Enter 'M' for Manager or 'S' for Sales (Q to quit): 

'''



