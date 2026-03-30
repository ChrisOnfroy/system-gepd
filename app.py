from services import *
from archive import *
from validations import *

print("Welcome to app!")


#This function, called “menu,” launches the program
def menu():

    isMenu = True

    while isMenu :

        try:
            menu = int(input("""
            Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  """))
            validationNum(menu)
            if menu == 1:
                addStudents()
            elif menu == 2:
                showStudents()
            elif menu == 3:
                searchStudents()
            elif menu == 4:
                updateStudents()
            elif menu == 5:
                deleteStudents()
            elif menu == 6:
                save_students()
            elif menu == 7:
                load_students()
            elif menu == 8:
                isMenu = False
                print("Program Close")
            else:
                print("")
                print("Enter a valid number")
                
        except ValueError:
            print("")
            print("Cant Enter emptys")

menu()