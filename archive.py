import csv

from services import Liststudent
# name of the archive where saves information about students
FILENAME = "data/listStudents.csv"

# this method is about save liststudents in filename.csv
def save_students():

    try:
        with open(FILENAME, 'a', newline='', encoding='utf-8') as file:

            fieldnames = ['identification', 'name', 'age', 'program', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            
            for student in Liststudent:
                writer.writerow(student)
        
        print(f"\n List Students saved successfully to '{FILENAME}'")
        return True
    
    except:
        print("\n Error saving students")
        return False


#this method is about load liststudents in filename.csv
def load_students():
    
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            
            reader = csv.DictReader(file)
            
            for row in reader:
                student = { 
                    "identification": int(row['identification']),
                    "name" : row['name'].strip().lower(),
                    "age" : int(row['age']),
                    "program" : row['program'].strip().lower(),
                    "status" :row['status']
                }
            
                Liststudent.append(student)
                
        return Liststudent
    
    except FileNotFoundError:
        print("\n File not found. Starting empty.")
        return Liststudent
    except:
        print("\n Error loading: ")
        return Liststudent