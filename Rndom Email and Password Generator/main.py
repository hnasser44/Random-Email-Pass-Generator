import random
import string

def CreateEmail(firstName,LastName):
    return firstName[0].upper() + LastName.title() + (str)(random.randint(0,999)) + "@gmail.com"
    
def CreatePassowrd(sizeofPass):
    letters = list(string.ascii_letters)
    symbols =  ['!','@','$'] + ['']*30
    password = ""
    for i in range(sizeofPass):
        num = random.randint(0,len(letters)-1)
        password += letters[num] + symbols[i]
    return password

def start():
    x = input("Hello, would you like to create a random generated email and password??... Enter (Y) or (N): ")
    if x=='N' or x=='n':
        return
    if x=='Y' or x=='y':
        first = input("OK then may I have your first Name please: ")
        last = input("and your last Name too: ")
        print("Your new email address is: ", end="")
        print(CreateEmail(first,last))
        size = int(input("What would you like the size of your password to be (MAX is 15): "))
        print("Your new password is: ", end="")
        print(CreatePassowrd(size))
start()
