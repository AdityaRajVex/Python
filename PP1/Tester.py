# Name: Aditya Raj
# File Name: Tester.py
# Date: 4/29/24
#
# Short Description: Test the Customer, Queue, CustomerTree classes
# Program description output
print('This program will test the Customer, Queue, CustomerTree classes\n')
# Initialize the data
from Customer import Customer
from CustomerTree import CustomerTree
from Queue import Queue
from Sport import Sport

s11 = Sport('Golf', 'S103', 399.99)
s12 = Sport('Swimming', 'S102', 29.99)
sport1 = [s11, s12]
c1 = Customer('Joe', 50, True, sport1)

s21 = Sport('Tennis', 'S101', 129.99)
s22 = Sport('Swimming', 'S102', 29.99)
s23 = Sport('Golf', 'S103', 399.99)
s24 = Sport('Dance', 'S106', 59.99)
sport2 = [s21, s22, s23, s24]
c2 = Customer('Ivy', 15, True, sport2)

s31 = Sport('Golf', 'S103', 399.99)
sport3 = [s31]
c3 = Customer('Sam', 70, True, sport3)

s41 = Sport('Golf', 'S103', 399.99)
s42 = Sport('Dance', 'S106', 59.99)
sport4 = [s41, s42]
c4 = Customer('June', 45, False, sport4)


s51 = Sport('Tennis', 'S101', 129.99)
s52 = Sport('Boating', 'S105', 199.99)
s53 = Sport('Dance', 'S106', 59.99)
sport5 = [s51, s52, s53]
c5 = Customer('Kate', 30, True, sport5)

s61 = Sport('Swimming', 'S102', 29.99)
s62 = Sport('Running', 'S104', 19.99)
sport6 = [s61, s62]
c6 = Customer('Aby', 55, False, sport6)

customers = [c1, c2, c3, c4, c5, c6]
if __name__ == '__main__':
    customer_queue = Queue()
    customer_queue.enqueue(c1)
    customer_queue.enqueue(c2)
    customer_queue.enqueue(c3)
    customer_queue.enqueue(c4)
    customer_queue.enqueue(c5)
    customer_queue.enqueue(c6)
    # Calculations
    CustomerTree = CustomerTree()
    end = False
    while not end:
        if customer_queue.isEmpty():
            end = True
        else:
            cur_customer = customer_queue.dequeue()
            CustomerTree.Add(cur_customer)
    CustomerTree.display()
    CustomerTree.remove(CustomerTree.search_age(50))
    CustomerTree.remove(CustomerTree.search_age(55))
    CustomerTree.display()


# Display results
'''
Testing run data:
This program will test the Customer, Queue, CustomerTree classes

Name: Aby
Age: 55
Fee: $99.98

Name: Sam
Age: 70
Fee: $304.99

Name: Kate
Age: 30
Fee: $322.98

Name: Joe
Age: 50
Fee: $350.99

Name: Ivy
Age: 15
Fee: $458.97

Name: June
Age: 45
Fee: $509.98



The customer with age 50 is removed

The customer with age 55 is removed

Name: Sam
Age: 70
Fee: $304.99

Name: Kate
Age: 30
Fee: $322.98

Name: Ivy
Age: 15
Fee: $458.97

Name: June
Age: 45
Fee: $509.98




Process finished with exit code 0
'''
