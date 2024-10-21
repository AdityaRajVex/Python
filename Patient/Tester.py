# Name: Aditya Raj
# File Name: Tester.py
# Date: 02/03/24
#
# Short Description: Calculate the average of 3 numbers
# Program description output
print('This program will keep the data of a patient and their procedures')

# Initialize the data
from Procedure import Procedure
from Patient import Patient

# Calculations
patient = Patient("Paddy Chung", "25 Yearsly Rd, Media, PA 19063", "610-999-8388 (Cell)", '610-999-8388')
Procedure1 = True
Procedure2 = False
Procedure3 = True

if Procedure1:
    procedure1 = Procedure("Physical Exam", "03/17/2024", "Dr. Irvine", 250.00)
    patient.add_procedure(procedure1)
if Procedure2:
    procedure2 = Procedure("X-ray", "03/17/2024", "Dr. Jamison", 500.00)
    patient.add_procedure(procedure2)
if Procedure3:
    procedure3 = Procedure("Blood test", "03/17/2024", "Dr. Smith", 200.00)
    patient.add_procedure(procedure3)




# Display results
print("Patient Name:", patient.get_name())
print("Address:", patient.get_address())
print("Phone:", patient.get_phone())
print("Emergency Contact:", patient.get_contact())
print("\nProcedures:")
for procedure in patient.get_procedures():
    print("\n- Procedure:", procedure.get_name())
    print("  Date:", procedure.get_date())
    print("  Practitioner:", procedure.get_practitioner())
    print("  Charges:", procedure.get_charges())
print("Total Charges:", patient.get_bill())

"""
testing run data:

    This program will keep the data of a patient and their procedures
    Patient Name: Paddy Chung
    Address: 25 Yearsly Rd, Media, PA 19063
    Phone: 610-999-8388 (Cell)
    Emergency Contact: 610-999-8388
    
    Procedures:
    
    - Procedure: Physical Exam
      Date: 03/17/2024
      Practitioner: Dr. Irvine
      Charges: 250.0
    
    - Procedure: Blood test
      Date: 03/17/2024
      Practitioner: Dr. Smith
      Charges: 200.0
    Total Charges: 450.0
    
    Process finished with exit code 0

"""