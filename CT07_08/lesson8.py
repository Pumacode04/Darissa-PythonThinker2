# print("Hello from lesson 8")

#Task Recap: 
#student_indexes = [1042, 1099, 1031, 1120,
#                    1075, 1042, 1108, 1019,
#                    1063, 1099, 1156, 1027,
#                    1084, 1111, 1031, 1143,
#                    1055, 1108, 1070, 1132,
#                    1055, 1168, 1020, 1084,
#                    1175]
#uniqueList = []
#dupe = 0
#for index in student_indexes:
#    if index not in uniqueList:
#        uniqueList.append(index)
#    else:
#        dupe += 1

#uniqueList = sorted(uniqueList)
#print(uniqueList)
#print(f"Duplicates : {dupe}")
#print(f"There are {len(uniqueList)} students.")

#Task 1:
#just notes below
#variable.isalpha() for confirming all are letters
#variable.isdigit() for confirming all are numbers
#for char in variable:
#   if not char.isdigit and not char.isalpha: (checking for special characters)
#       vaild = False

#Actual task
#Task 1a:
#name = ""
#while True:
#    name = input("Enter your first name.")
#    if name.isalpha():
#        print("Valid.")
#        break
#    else:
#        print(("Invalid. Try Again."))

#Task 1b:
#age = 0
#while True:
#    age = input("What's your age?")
#    if age.isdigit():
#        print("Valid.")
#        break
#    else:
#        print("Invalid. Try Again.")
     
#Task 1c:
#username = ""
#while True:
#    username = input("Create a username.")
#    if username.isalnum():
#        print("Valid.")
#        break
#    else:
#        print("Invalid. Try Again.")

#Task 2a:
#hp = 0
#while True:
#    hp = input("Enter your phone number.")
#    if len(hp) == 8 and hp.isdigit():
#        print("Valid.")
#        break
#    else:
#        print("Invalid. Try Again.")

#Task 2b:
#user = ""
#while True:
#    user = input("Enter your username.")
#    if len(user) < 18 and len(user) > 5:
#        print("Valid.")
#        break
#    else:
#        print("Invalid. Try Again.")

#Task 3a:
#year = 0
#while True:
#    year = input("Enter your birth year.")
#    if volume.isdigit() and int(year) > 1900 and int(year) < 2026:
#        print("Valid")
#        break
#    else:
#        print("Invalid. Try Again.")

#Task 3b:
#volume = 0
#while True:
#    volume = input("Enter your volume setting.")
#    if volume.isdigit() and int(volume) > 0 and int(volume) < 100:
#        print("Valid")
#        break
#    else:
#        print("Invalid. Try Again.")

#Task 4a:
#sentence = ""
#mocking = ""
#counter = 0
#sentence = input("Give me a sentence.")
#for char in sentence:
#    if char.isalpha():
#        if counter % 2 == 0:
#            char = char.upper()
#        else:
#            char = char.lower()
#        mocking = mocking + char
#        counter += 1
#    else:
#        mocking = mocking + char
#print(mocking)

#Task 5:
#word = "SINGAPORE"
#print(word[0:4])
#print(word[3:6])
#print(word[5:])
#print(word[0:9:2])

#Task 6:
#word = ""
#reverso = word[::-1]
#while True:
#    word = input("Enter a word.")
#    reverso = word[::-1]
#    if word == "end":
#        break
#    if word == reverso:
#        print("This word is a panlindrone.")
#    else:
#        print("This word is not a panlindrone.")

#Task 7:
#friends = ["Amanda", "Braelyn", "Cheryl"]
#user = input("Name : ")
#while user.strip() == "":
#    print("Invaild name. Try Again.")
#    user = input("Name : ")
#
#if user in friends:
#    print("You may come in.")
#else:
#    print("Go Home.")

#Task 8:
#first_last_upper = False
#first_letter_valid = False
#digit_7 = False
#char_9 = False

#while True:
#    nric = input("Enter your nric.")
#    if nric.strip() == "":
#        print("NRIC cannot be empty. Try Again.")
#    elif len(nric) != 9:
#        print("NRIC should have 9 characters. Try Again.")
#    else:
#        char_9 = True
#        print("Has 9 char")
#        break

#if nric[0].isupper() and nric[8].isupper():
#    first_last_upper = True
#    print("First and last upper")
#if nric[0] == "S" or nric[0] == "T" or nric[0] == "F" or nric[0] == "G" or nric[0] == "M":
#    first_letter_vaild = True
#    print("First letter valid")
#if nric[1:8].isdigit():
#    digit_7 = True
#    print("Has 7 num")
##if len(nric) == 9:
##    char_9 = True

#if first_last_upper and first_letter_vaild and digit_7 and char_9:
#    print("NRIC is vaild.")
#else:
#    print("NRIC is NOT vaild.")

#Task 9:
char8 = False
upLow = False
num = False
upper = False
lower = False
noSpecialChar = False

password = input("Enter a password. ")
if len(password) >= 8:
    char8 = True

for char in password:
    if char.isalpha():
        if char.isupper():
            upper = True
        if char.islower():
            lower = True
    if upper and lower:
        upLow = True
    if char.isdigit():
        num = True
    if char.isalpha() or char.isdigit():
        noSpecialChar = True
    else:
        noSpecialChar = False
        break

if char8 and upLow and num and noSpecialChar:
    print("Password successfully set.")
else:
    print("Your password did not meet requirements.")