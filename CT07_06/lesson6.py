#print("Hello from lesson 6")
#Task Recap
#import random

#uniqueNum = []
#notSoLuckyNumbers = 0
#notSoLuckyNumbers = random.randint(1, 1000)
#sumOfNum = 0

#while len(uniqueNum) < 101:
#    if notSoLuckyNumbers in uniqueNum:
#        notSoLuckyNumbers = random.randint(1, 1000)
#    else:
#        uniqueNum.append(notSoLuckyNumbers)
#        sumOfNum = sumOfNum + notSoLuckyNumbers

#print(uniqueNum)
#print(max(uniqueNum))
#print(min(uniqueNum))
#print(sumOfNum/len(uniqueNum))
#print(uniqueNum[random.randint(1,100)])

#Task 1:
#contacts = []
#contact1 = ["John", 98453126, "john@gmail.com"]
#contact2 = ["Adam", 93029102, "adam@gmail.com"]
#contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]
#contacts.append(contact1)
#contacts.append(contact2)
#contacts.append(contact3)
#for contact in contacts:
#    for info in contact:
#        print(info)

#Task 2:
#students = [
#    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
#]

#for student in students:
#    name, gender = student
#    print(f"Gender of {name}: {gender}")

#Task 3:
students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]
girls = []
boys = []

for student in students:
    name, gender = student

    if gender == "F":
        girls.append(name)
    else:
        boys.append(name)

for i in girls:
    print(i)

print(f"There are {len(girls)} girls.")

for i in boys:
    print(i)

print(f"There are {len(boys)} boys.")