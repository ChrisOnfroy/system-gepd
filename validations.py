
#this validations is about strings
def validationName(nameEstudent):
    if nameEstudent.isalpha():
        return False
    else:
        print("")
        print("Error: the name student cant empty and not numbers")
        return True
    
#this validation is about numbers
def validationNum(num):
    if num > 0:
        return False

    else:
        print("")
        print("Error: the price to product is only positive")

    
