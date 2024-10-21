# Name: Aditya Raj
# File Name: Grade_Tester.py
# Date: 01/22/2024
#
# Short Description: Calculate the average Grade and return the according Letter
# Program description output
print(f'This program takes in 5 grades and finds out the corresponding letter grade by calculating the average')

# Initialize the data
import random
import Grade
grades = []

# Calculations
for i in range(5):
    grades.append(random.randint(0, 100))

avg = Grade.calc_avg(grades)
print(f'The average grade is: {avg:.1f}')
letter_grade = Grade.converter(avg)
print(f'The letter grade is:', letter_grade)

# Display results
'''
Testing run data:
Trial 1:
    This program takes in 5 grades and finds out the corresponding letter grade by calculating the average
    The average grade is: 49.6
    The letter grade is: F
    
    Process finished with exit code 0

Trial 2:
    This program takes in 5 grades and finds out the corresponding letter grade by calculating the average
    The average grade is: 84.2
    The letter grade is: B
    
    Process finished with exit code 0

Trial 3:
    This program takes in 5 grades and finds out the corresponding letter grade by calculating the average
    The average grade is: 69.4
    The letter grade is: D
    
    Process finished with exit code 0

'''