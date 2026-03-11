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
sentence = ""
mocking = ""
counter = 0
sentence = input("Give me a sentence.")
for char in sentence:
    if char.isalpha:
        if counter / 2 == 0:
            char = char.upper()
        else:
            char = char.lower()
        mocking = char + mocking
        counter += 1
print(mocking)