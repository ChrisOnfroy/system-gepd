from validations import *

#in this list you see all students 
Liststudent = []


#this method add students 
def addStudents():


    validateId = True
    while validateId :
        idEstudent = int(input("\nEnter number of identification: "))
        validateId = validationNum(idEstudent)

    validateName = True
    while validateName:
        nameEstudent = input("\nEnter name to student: ").lower().strip()
        validateName = validationName(nameEstudent)
    
    
    validateAge = True  
    while validateAge:
        try:

            ageEstudent = int(input("\nEnter age: "))
            validateAge = validationNum(ageEstudent)

        except ValueError:
            print("Error: please enter a valide number")

    validateProgram = True 
    while validateProgram:

        programEstudent = input("\nEnter progam of the estudent: ")
        validateProgram = validationName(programEstudent)

    validateStatus = True
    while validateStatus:

        status = False
        statusEstudent = input("\nEnter the status of the student(FALSE OR TRUE): ").lower()
        if statusEstudent == "true":
            status = True
            validateStatus = False
        elif statusEstudent == "false":
            status = False
            validateStatus = False
        else:
            validateStatus = True
            print("Enter Status Valid")

        

        student = { 
                    "identification": idEstudent,
                    "name" : nameEstudent,
                    "age" : ageEstudent,
                    "program" : programEstudent,
                    "status" :status
                }
    
        Liststudent.append(student)


#this method show all students 
def showStudents():
    
    for student in Liststudent:

        print(f"""\n
                identification: {student['identification']} 
                name: {student['name']} 
                age: {student['age']}
                program: {student['program']}
                status: {student['status']}
            """)


#this method serach student by name.
def searchStudents():

    search = input("Enter name student: ").lower().strip()
    exist = False

    for student in Liststudent:

        if student["name"] == search:
            print(f"""\n
                identification: {student['identification']} 
                name: {student['name']} 
                age: {student['age']}
                program: {student['program']}
                status: {student['status']}
            """)
            exist = True
            return True  
    
    if not exist:
        print("Student name not found.")
        return False  
    
#update student by name
def updateStudents():

    search = input("Enter name student: ").lower().strip()
    exist = False

    for student in Liststudent:
        if student["name"] == search:
            print(f"""\n
                identification: {student['identification']} 
                name: {student['name']} 
                age: {student['age']}
                program: {student['program']}
                status: {student['status']}
            """)

            validateAge = True  
            while validateAge:
                try:
                    newAge = int(input("\nEnter new Age: "))
                    validateAge = validationNum(newAge)
                except ValueError:
                    print("Error: please enter a valide number")

            validateProgram = True 
            while validateProgram:
                newProgram = input("\nEnter new Program: ").lower()
                validateProgram = validationName(newProgram)

            newstatus = False
            validateStatus = True
            while validateStatus:
                changeStatus = input("\nEnter new Status: ").lower()
                if changeStatus == "true":
                    newstatus = True
                    validateStatus = False
                elif changeStatus == "false":
                    newstatus = False
                    validateStatus = False
                else:
                    validateStatus = True
                    print("\nEnter a valid status")
            
            student['age'] = newAge
            student['program'] = newProgram
            student['status'] = newstatus 

            exist = True
            return True
        if not exist:
            print("Student name not found.")
            return False
        

# delete students whit name 
def deleteStudents():
    search = input("Enter name student to delete: ").lower().strip()
    exist = False
    for i, student in enumerate(Liststudent):
        if student["name"] == search:
                print(f"""\n
                    identification: {student['identification']} 
                    name: {student['name']} 
                    age: {student['age']}
                    program: {student['program']}
                    status: {student['status']}
                """)
                
                confirm = input("\nAre you sure you want to delete this student? (y/n): ").lower().strip()
                
                if confirm == 'y':
                    deleted = Liststudent.pop(i)
                    print(f"\nStundent '{deleted['name']}' has been deleted successfully!")
                    return True
                else:
                    print("Deletion cancelled.")
                    return False
        if not exist:
            print("Student name not found.")
            return False
        