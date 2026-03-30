# Student Management System with Data Persistence

This programa is a basic students managment in where you do certains tasks and you do archive the information about students

## What does the program do?

- The program add students to the listStudents.
- Validates that the name is not empty or numeric, and that identification and age are positive numbers.
- Show students of the list if was added
- search for specific student by name
- Update existing student information
- Delete student with confirmation
- Save Students to a CSV file
- Load Students from a CSV file

## Example usage

### Menu

```text
    Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  
```

### Add Student

```text

    Enter number of identification: 1041691420

    Enter name to student: Cristian

    Enter age: 21

    Enter progam of the estudent: adso

    Enter the status of the student(FALSE OR TRUE): true

```

### Show Students

```text
        Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  2


                identification: 1041691420 
                name: cristian 
                age: 21
                program: adso
                status: True
            
```

### Search Student

```text

            Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  3
            
            Enter name student: Cristian

                identification: 1041691420 
                name: cristian 
                age: 21
                program: adso
                status: True

```

### Updte Student

```text

        Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  4
            Enter name student: cristian


                identification: 1041691420 
                name: cristian 
                age: 24
                program: coder
                status: False
            

                Enter new Age: 21

                Enter new Program: coder

                Enter new Status: true

```

### Delete Student

```text
        Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  5
            Enter name student to delete: cristian


                    identification: 1041691420 
                    name: cristian 
                    age: 21
                    program: coder
                    status: True
                

            Are you sure you want to delete this student? (y/n): y

            Stundent 'cristian' has been deleted successfully!

```

### Save Student to Csv

```text
        Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  6

        List Students saved successfully to 'data/listStudents.csv'
```

### Load listStudents.csv to program

```text
        Please enter a digit number (1-8) :
            1. Create Student
            2. Students List
            3. Search Student
            4. Update Student
            5. Delete Student
            6. Save Students
            7. Load Students
            8. Exit
            Enter →  7
```
