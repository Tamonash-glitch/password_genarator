import random 
import string
def passwordgenrator(min_length,numbers=True,special=True):
    letters=string.ascii_letters
    digits=string.digits
    specialcharacters=string.punctuation
    characters=letters
    if numbers:
        characters+=digits
    if special:
        characters+=specialcharacters
    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False
    while not meets_criteria or len(pwd)<min_length:
        newchar=random.choice(characters)
        pwd+=newchar
        if newchar in digits:
            has_number=True
        if newchar in specialcharacters:
            has_special=True
        meets_criteria = True
        if numbers:
            meets_criteria=has_number
        if special:
            meets_criteria=meets_criteria and has_special
    return pwd
minimumlength=int(input("enter the minimum lenght of the password you want to generate "))
number=input("should it have numbers: y/n ").lower()=="y"
special=input("should it have special: y/n ").lower()=="y"
print(passwordgenrator(minimumlength,number,special))


        
