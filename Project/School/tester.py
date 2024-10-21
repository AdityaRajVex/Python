# Name: Aditya Raj
# File Name: tester.py
# Date: 3/31/24
#
# Description: Tester module to add, edit, delete, and display Students
from Student import Student
from MailingAddress import MailingAddress
from Email import Email
from Phone_number import Phone_number
from Date import Date
from Semester import Semester
from Advisor import Advisor
from Course import Course
from LinkedList import LinkedList


# Function to create a MailingAddress object based on user input
def createAddress():
    street = input("Please enter the street address: ")
    city = input("Please enter the city: ")
    state = input("Please enter the state: ")
    zip = input("Please enter the zip code: ")
    type = input("Please enter the residence type: ")
    return MailingAddress(street, city, state, zip, type)


# Function to create and append Email objects to a given list based on user input
def createEmail(emails):
    email = input("Please enter the email address: ")
    type = input("Please enter the email type: ")
    cont = input("Do you want to enter another email (y/n): ")
    emails.append(Email(email, type))
    if cont == "y":
        return createEmail(emails)


# Function to create and append Phone_number objects to a given list based on user input
def createPhone(phones):
    phone = input("Please enter the phone number: ")
    type = input("Please enter the phone type: ")
    cont = input("Do you want to enter another phone (y/n): ")
    phones.append(Phone_number(phone, type))
    if cont == "y":
        return createPhone(phones)


# Function to create a Date object based on user input
def createDate():
    month = input("Please enter the month: ")
    day = input("Please enter the day: ")
    year = input("Please enter the year: ")
    return Date(month, day, year)


# Function to create a Semester object based on user input
def createSemester():
    semester = input("Please enter the starting semester: ")
    year = input("Please enter the starting year: ")
    return Semester(semester, year)


# Function to create a Advisor object based on user input
def createAdvisor():
    Loop = True
    AdviseesLinkedList = LinkedList()
    first_name = input("Please enter the first name:  ")
    middle_name = input("Please enter the middle name:  ")
    last_name = input("Please enter the last name:  ")
    title = input("Please enter the title:  ")
    department = input("Please enter the department:  ")
    while Loop:
        add = input("Add a student as an advisee y/n:  ")
        if add.upper() == 'Y':
            choices = 'add as an advisee'
            advisee = selectStudent(choices)
            AdviseesLinkedList.insert(advisee)
        else:
            Loop = False
    if middle_name == '':
        return Advisor(first_name, last_name, title, department, AdviseesLinkedList)
    else:
        return Advisor(first_name, last_name, title, department, AdviseesLinkedList, middle_name)



# Function to create a Course object based on user input
def createCourse():
    choice = True
    CourseLinkedList = LinkedList()
    while choice:
        add = input("Enter Y to add a course:  ")
        if add.upper() == 'Y':
            course_name = input("Please enter the course name:  ")
            semester_taken = input("Please enter the Semester taken:  ")
            style = input("Please enter the Style:  ")
            status = input("Please enter the status:  ")
            grade = input("Please enter the grade:  ")
            curr = Course(course_name, semester_taken, style, status, grade)
            CourseLinkedList.insert(curr)
        else:
            choice = False
    return CourseLinkedList



# Function to display a list of current students and check if the user selected ID exists in the list
def selectStudent(choice):
    print("\nCurrent Students:")
    for student in students:
        print(f"{student.getName()} (ID: {student.getID()})")
    studentID = input(f"Enter the ID of the Student to {choice}: ")
    exists = False
    for student in students:
        if student.getID() == studentID:
            exists = True
            return student
        else:
            exists = False
    if not exists:
        print("Invalid ID")
        return False

# Function to select advisor
def selectAdvisorln(choice):
    print("\nCurrent Advisors:")
    for advisor in advisors:
        print(f"{advisor.getFirst_name()} {advisor.getLast_name()}")
    chosen = input(f"Enter the last name of the Advisor to {choice}: ")
    exists = False
    for advisor in advisors:
        if advisor.getLast_name() == chosen:
            exists = True
            return advisor.getLast_name()
        else:
            exists = False
    if not exists:
        print("Invalid ID")
        return False

def selectAdvisor(choice):
    print("\nCurrent Advisors:")
    for advisor in advisors:
        print(f"{advisor.getFirst_name()} {advisor.getLast_name()}")
    chosen = input(f"Enter the last name of the Advisor to {choice}: ")
    exists = False
    for advisor in advisors:
        if advisor.getLast_name() == chosen:
            exists = True
            return advisor
        else:
            exists = False
    if not exists:
        print("Invalid ID")
        return False

# Menu to add students based on user input
def addStudentMenu():
    name = input("Enter Student Name: ")
    id = input("Enter Student ID: ")
    print("Enter Address")
    address = createAddress()
    emails = []
    phones = []
    createEmail(emails)
    createPhone(phones)
    print("Enter your birthday")
    birth_date = createDate()
    print("Enter your acceptance day")
    acceptance_date = createDate()
    print("Enter starting semester and year")
    semester = createSemester()
    major = input("Please enter you intended major: ")
    print("Enter courses: ")
    courses = createCourse()
    students.append(Student(name, id, address, emails, phones, birth_date, acceptance_date, semester, major, courses))
    cont = input("Add another student (y/n): ")
    if cont == 'y':
        addStudentMenu()
    elif cont == 'n':
        mainMenu()
    else:
        print("Invalid Input")
        mainMenu()


# Menu to edit students based on user input
def editStudentMenu(id):
    for student in students:
        if student.getID() == id:
            print("What would you like to edit:"
                  f"\n1) Name"
                  f"\n2) ID"
                  f"\n3) Mailing Address"
                  f"\n4) Email"
                  f"\n5) Phone Number"
                  f"\n6) Birth Date"
                  f"\n7) Acceptance Date"
                  f"\n8) Semester Start"
                  f"\n9) Intended Major"
                  f"\n10) Courses"
                  f"\n11) Advisor"
                  f"\n12) Return to Main menu")
            edit = input("")
            if edit == "1":
                print(f"Current Name: {student.getName()}")
                name = input("Enter new Student Name: ")
                student.setName(name)
                editStudentMenu(id)
            elif edit == "2":
                print(f"Current ID: {student.getID()}")
                id = input("Enter new Student ID: ")
                student.setID(id)
                editStudentMenu(id)
            elif edit == "3":
                print(f"Current Address: {student.getMailingAddress().__str__()}")
                street = input("Enter new street address (Enter to skip): ") or student.getMailingAddress().getStreet()
                student.getMailingAddress().setStreet(street)
                city = input("Enter new city (Enter to skip): ") or student.getMailingAddress().getCity()
                student.getMailingAddress().setCity(city)
                state = input("Enter new state (Enter to skip): ") or student.getMailingAddress().getState()
                student.getMailingAddress().setState(state)
                zip = input("Enter new zip code (Enter to skip): ") or student.getMailingAddress().getZipCode()
                student.getMailingAddress().setZipCode(zip)
                type = input("Enter new residence type (Enter to skip): ") or student.getMailingAddress().getType()
                student.getMailingAddress().setType(type)
                editStudentMenu(id)
            elif edit == "4":
                change = input("Edit existing email or add new email (e/a): ")
                if change == 'a':
                    emails = student.getEmail()
                    createEmail(emails)
                    editStudentMenu(id)
                elif change == 'e':
                    print("Current Emails:")
                    for i in range(len(student.getEmail())):
                        print(f"{i + 1}) {student.getEmail()[i]}")
                    email = int(input("Choose email to edit: "))
                    if 1 <= email <= len(student.getEmail()):
                        emailAddress = input("Enter new email (Enter to skip): ") or student.getEmail()[
                            email - 1].getEmailAddress()
                        student.getEmail()[email - 1].setEmailAddress(emailAddress)
                        type = input("Enter new email type (Enter to skip): ") or student.getEmail()[
                            email - 1].getType()
                        student.getEmail()[email - 1].setType(type)
                        editStudentMenu(id)
                    else:
                        print("Invalid Input")
                        editStudentMenu(id)
                else:
                    print("Invalid Input")
                    editStudentMenu(id)
            elif edit == "5":
                change = input("Edit existing phone or add new phone (e/a): ")
                if change == 'a':
                    phones = student.getPhoneNumber()
                    createPhone(phones)
                    editStudentMenu(id)
                elif change == 'e':
                    print("Current Phones:")
                    for i in range(len(student.getPhoneNumber())):
                        print(f"{i + 1}) {student.getPhoneNumber()[i]}")
                    phone = int(input("Choose phone to edit: "))
                    if 1 <= phone <= len(student.getPhoneNumber()):
                        phoneNumber = input("Enter new phone number (Enter to skip): ") or student.getPhoneNumber()[
                            phone - 1].getNumber()
                        student.getPhoneNumber()[phone - 1].setNumber(phoneNumber)
                        type = input("Enter new phone type (Enter to skip): ") or student.getPhoneNumber()[
                            phone - 1].getPhoneType()
                        student.getPhoneNumber()[phone - 1].setPhoneType(type)
                        editStudentMenu(id)
                    else:
                        print("Invalid Input")
                        editStudentMenu(id)
                else:
                    print("Invalid Input")
                    editStudentMenu(id)
            elif edit == "6":
                print(f"Current Birth Date: {student.getBirthDate().__str__()}")
                date = createDate()
                student.setBirthDate(date)
                editStudentMenu(id)
            elif edit == "7":
                print(f"Current Acceptance Date: {student.getAcceptanceDate().__str__()}")
                date = createDate()
                student.setAcceptanceDate(date)
                editStudentMenu(id)
            elif edit == '8':
                print(f"Current semester start: {student.getSemesterStart().__str__()}")
                semester = createSemester()
                student.setSemesterStart(semester)
                editStudentMenu(id)
            elif edit == '9':
                print(f"Current intended major: {student.getIntendedMajor()}")
                major = input("Enter the new intended major: ")
                student.setIntendedMajor(major)
                editStudentMenu(id)
            elif edit == '10':
                change = input("Are you sure you want to assign new courses y/n: ")
                if change.upper() == 'Y':
                    newCourses = createCourse()
                    student.setCourses(newCourses)
                    editStudentMenu(id)
                else:
                    print("Invalid Input")
                    editStudentMenu(id)
            elif edit == '11':
                mainMenu()
            else:
                print("Invalid Input")
                editStudentMenu(id)

def editAdvisorMenu(last_name):
    for advisor in advisors:
        if advisor.getLast_name() == last_name:
            print("What would you like to edit:"
                  f"\n1) First name"
                  f"\n2) Middle name"
                  f"\n3) Last name"
                  f"\n4) Title"
                  f"\n5) Department"
                  f"\n6) advisees"
                  f"\n7) Return to Main menu")
            edit = input("")
            if edit == "1":
                print(f"Current Name: {advisor.getLast_name()}")
                firstname = input("Enter new First Name: ")
                advisor.setFirst_name(firstname)
                editAdvisorMenu(last_name)
            if edit == "2":
                print(f"Current Name: {advisor.getMiddle_name()}")
                middlename = input("Enter new Middle Name: ")
                advisor.setMiddle_name(middlename)
                editAdvisorMenu(last_name)
            if edit == "3":
                print(f"Current Name: {advisor.getLast_name()}")
                lastname = input("Enter new Last Name: ")
                advisor.setLast_name(lastname)
                mainMenu()
            if edit == "4":
                print(f"Current Title: {advisor.getTitle()}")
                title = input("Enter new Title: ")
                advisor.setLast_name(title)
                editAdvisorMenu(last_name)
            if edit == "5":
                print(f"Current Department: {advisor.getDepartment()}")
                Department = input("Enter new Department: ")
                advisor.setDepartment(Department)
                editAdvisorMenu(last_name)
            if edit == "6":
                choice = input("Edit existing or add advisees (e/a):  ")
                if choice.upper() == 'E':
                    print(advisor.getAdvisees())
                    cho = input('Enter the ID of the student to remove: ')
                    advisor.execute_delete(cho)
                    editAdvisorMenu(last_name)

                elif choice.upper() == 'A':
                    Loop = True
                    while Loop:
                        add = input("Add a student as an advisee y/n:  ")
                        if add.upper() == 'Y':
                            choices = 'add as an advisee'
                            student = selectStudent(choices)
                            advisor.execute_insert(student.getID())
                        else:
                            Loop = False
                    editAdvisorMenu(last_name)
                else:
                    editAdvisorMenu(last_name)
            if edit == "7":
                mainMenu()



# Main menu to select either to add, edit, delete, or display students
def mainMenu():
    print("\n"
          "What would you like to do:"
          f"\n1) Add Student"
          f"\n2) Edit Student"
          f"\n3) Delete Student"
          f"\n4) Display Student"
          f"\n5) Add Advisor"
          f"\n6) Display Advisor"
          f"\n7) Edit Advisor"
          f"\n8) Exit")
    choice = input("")
    if choice == '1':
        addStudentMenu()
    elif choice == '2':
        if not students:
            print("No students to edit")
            mainMenu()
        else:
            student = selectStudent("edit")
            if student:
                editStudentMenu(student.getID())
            else:
                mainMenu()
    elif choice == '3':
        if not students:
            print("No students to delete")
            mainMenu()
        else:
            student = selectStudent("delete")
            if student:
                ask = input(f'Are you sure you want to delete {student.getName()} (ID: {student.getID()})?\n'
                            f'Enter y for yes: ')
                if ask.upper() == 'Y':
                    students.remove(student)
                    print(f'Successfully deleted {student.getName()} (ID: {student.getID()})')
                    mainMenu()
                else:
                    mainMenu()
            else:
                mainMenu()
    elif choice == '4':
        if not students:
            print("No students to display")
            mainMenu()
        else:
            student = selectStudent("display")
            if student:
                print(student)
                chosen = input('Display a list of courses y/n ')
                if chosen.upper() == 'Y':
                    print(student.getCourses())
                    print('courses printed \n')
                mainMenu()
            else:
                mainMenu()
    elif choice == '5':
        newad = createAdvisor()
        advisors.append(newad)
        mainMenu()
    elif choice == '6':
        if not advisors:
            print("No advisors to display")
            mainMenu()
        else:
            advisor = selectAdvisor("display")
            if advisor:
                print(advisor)
                chosen = input('Display a list of advisee y/n ')
                if chosen.upper() == 'Y':
                    print(advisor.getAdvisees())
                    print('Students printed based on the ID\n')
                mainMenu()
            else:
                mainMenu()
    elif choice == '7':
        if not advisors:
            print('No advisors to display')
            mainMenu()
        else:
            curAdv = selectAdvisorln('edit')
            editAdvisorMenu(curAdv)
    elif choice == '8':
        print("Thanks you for using this program")
    else:
        print("Invalid Input")
        mainMenu()


# Main
if __name__ == "__main__":
    a1 = MailingAddress("Street 1", "City1", "State1", "11111", "permanent")
    e1 = Email("Email1@email.com", "personal")
    p1 = Phone_number("111-111-1111", "Cell")
    bd1 = Date('1','1','2000')
    ad1 = Date('1','1','2018')
    sm1 = Semester("Fall",'2019')
    Course1List = LinkedList()
    Course1List.insert('Math')
    Course1List.insert('Chemistry')
    Course1List.insert('English')
    Course1List.insert('Physics')
    Course1List.insert('Computer Science')
    s1 = Student("Student 1", "1", a1, [e1],[p1], bd1, ad1, sm1, "Computer Science", Course1List)

    a2 = MailingAddress("Street 2", "City2", "State2", "22222", "permanent")
    e2 = Email("Email2@email.com", "personal")
    p2 = Phone_number("222-222-2222", "Cell")
    bd2 = Date('2', '2', '2000')
    ad2 = Date('2', '2', '2018')
    sm2 = Semester("Fall", '2019')
    Course2List = LinkedList()
    Course2List.insert('Math')
    Course2List.insert('English')
    Course2List.insert('Physics')
    Course2List.insert('Psychology')
    Course2List.insert('Computer Science')
    s2 = Student("Student 2", "2", a2, [e2], [p2], bd2, ad2, sm2, "Computer Science", Course2List)

    a3 = MailingAddress("Street 3", "City3", "State3", "33333", "permanent")
    e3 = Email("Email3@email.com", "personal")
    p3 = Phone_number("333-333-3333", "Cell")
    bd3 = Date('3', '3', '2000')
    ad3 = Date('3', '3', '2018')
    sm3 = Semester("Fall", '2019')
    Course3List = LinkedList()
    Course3List.insert('Math')
    Course3List.insert('English')
    Course3List.insert('Physics')
    Course3List.insert('Psychology')
    Course3List.insert('Computer Science')
    s3 = Student("Student 3", "3", a3, [e3], [p3], bd3, ad3, sm3, "Computer Science", Course3List)

    a4 = MailingAddress("Street 4", "City4", "State4", "44444", "permanent")
    e4 = Email("Email4@email.com", "personal")
    p4 = Phone_number("444-444-4444", "Cell")
    bd4 = Date('4', '4', '2000')
    ad4 = Date('4', '4', '2018')
    sm4 = Semester("Fall", '2019')
    Course4List = LinkedList()
    Course4List.insert('Math')
    Course4List.insert('Physics')
    Course4List.insert('Computer Science')
    s4 = Student("Student 4", "4", a4, [e4], [p4], bd4, ad4, sm4, "Computer Science", Course4List)

    a5 = MailingAddress("Street 5", "City5", "State5", "55555", "permanent")
    e5 = Email("Email5@email.com", "personal")
    p5 = Phone_number("555-555-5555", "Cell")
    bd5 = Date('5', '5', '2000')
    ad5 = Date('5', '5', '2018')
    sm5 = Semester("Fall", '2019')
    Course5List = LinkedList()
    Course5List.insert('Math')
    Course5List.insert('Physics')
    Course5List.insert('Psychology')
    Course5List.insert('Computer Science')
    s5 = Student("Student 5", "5", a5, [e5], [p5], bd5, ad5, sm5, "Computer Science", Course5List)

    first_name = 'Ronan'
    last_name = 'Fall'
    title = 'professor'
    department = 'Math'
    # Add in the advisee list as the student id number
    myAdvisee1List = LinkedList()
    myAdvisee1List.insert('1')
    myAdvisee1List.insert('2')
    ad1 = Advisor(first_name, last_name, title, department, myAdvisee1List)

    first_name = 'Thomas'
    last_name = 'James'
    title = 'Professor'
    department = 'CS'
    # Add in the advisee list as the student id number
    myAdvisee2List = LinkedList()
    myAdvisee2List.insert('3')
    myAdvisee2List.insert('4')
    myAdvisee2List.insert('5')
    middle_name = 'White'
    ad2 = Advisor(first_name, last_name, title, department, myAdvisee2List,middle_name)

    students = [s1, s2, s3, s4, s5]
    advisors = [ad1, ad2]
    mainMenu()

"""
testing run data:
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    5
    Please enter the first name:  Joe
    Please enter the middle name:  
    Please enter the last name:  Seph
    Please enter the title:  Prof
    Please enter the department:  Math
    Add a student as an advisee y/n:  y
    
    Current Students:
    Student 1 (ID: 1)
    Student 2 (ID: 2)
    Student 3 (ID: 3)
    Student 4 (ID: 4)
    Student 5 (ID: 5)
    Enter the ID of the Student to add as an advisee: 2
    Add a student as an advisee y/n:  n
    
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    5
    Please enter the first name:  Ad
    Please enter the middle name:  
    Please enter the last name:  Ra
    Please enter the title:  Proff
    Please enter the department:  CS
    Add a student as an advisee y/n:  n
    
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    6
    
    Current Advisors:
    Ronan Fall
    Thomas James
    Joe Seph
    Ad Ra
    Enter the last name of the Advisor to display: Fall
    Name: Ronan Fall
    Title: professor
    Department: Math
    
    Display a list of advisee y/n y
    1->2->None
    Students printed based on the ID
    
    
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    6
    
    Current Advisors:
    Ronan Fall
    Thomas James
    Joe Seph
    Ad Ra
    Enter the last name of the Advisor to display: James
    Name: Thomas White James
    Title: Professor
    Department: CS
    
    Display a list of advisee y/n y
    3->4->5->None
    Students printed based on the ID
    
    
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    7
    
    Current Advisors:
    Ronan Fall
    Thomas James
    Joe Seph
    Ad Ra
    Enter the last name of the Advisor to edit: Fall
    What would you like to edit:
    1) First name
    2) Middle name
    3) Last name
    4) Title
    5) Department
    6) advisees
    7) Return to Main menu
    6
    Edit existing or add advisees (e/a):  e
    1->2->None
    Enter the ID of the student to remove: 2
    It is deleted!
    What would you like to edit:
    1) First name
    2) Middle name
    3) Last name
    4) Title
    5) Department
    6) advisees
    7) Return to Main menu
    7
    
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    6
    
    Current Advisors:
    Ronan Fall
    Thomas James
    Joe Seph
    Ad Ra
    Enter the last name of the Advisor to display: Fall
    Name: Ronan Fall
    Title: professor
    Department: Math
    
    Display a list of advisee y/n y
    1->None
    Students printed based on the ID
    
    
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    4
    
    Current Students:
    Student 1 (ID: 1)
    Student 2 (ID: 2)
    Student 3 (ID: 3)
    Student 4 (ID: 4)
    Student 5 (ID: 5)
    Enter the ID of the Student to display: 2
    Name: Student 2
    ID: 2
    Mailing Address: Street 2, City2, State2 22222 (permanent)
    Email: Email2@email.com (personal)
    
    Phone: 222-222-2222 (Cell)
    
    Birth Date: 2/2/2000
    Acceptance Date: 2/2/2018
    Semester Start: Fall 2019
    Intended Major: Computer Science
    Display a list of courses y/n y
    Computer Science->English->Math->Physics->Psychology->None
    courses printed 
    
    
    What would you like to do:
    1) Add Student
    2) Edit Student
    3) Delete Student
    4) Display Student
    5) Add Advisor
    6) Display Advisor
    7) Edit Advisor
    8) Exit
    8
    Thanks you for using this program
    
    Process finished with exit code 0

"""
