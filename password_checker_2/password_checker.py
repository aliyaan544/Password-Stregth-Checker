import re
def check_the_pass(passw):
    strength = 0
    #checking length
    if len(passw) >= 8:
        strength += 1
    else:
        print("password too short")
    #checking upper and lower case
    if re.search("[a-z]",passw) and re.search("[A-Z]",passw):
        strength +=1
    else:
        print("use combination of upper and lowercase letters")
    #checking numbers
    if re.search("[0-9]",passw):
        strength +=1
    else:
        print("include some numbers")
    #checking special characters
    if re.search("[!@#$%^&*()_+]",passw):
        strength +=1
    else:
        print("add special characters")
    #final strength
    if strength == 4:
        print("strong password")
    elif strength == 3:
        print("medium password")
    elif strength == 2:
        print("very easy password make a stronger one")
password = input("enter your password to check strength")
check_the_pass(password)

