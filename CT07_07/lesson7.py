#print("Hello from lesson 7")
#Recap ahh
#students = []

#student1 = ["Cheryl", "12345678", "Badminton"]
#student2 = ["Yati", "39401342", "Science Club"]
#student3 = ["Amanda", "80142424", "Art & Craft"]

#students.append(student1)
#students.append(student2)
#students.append(student3)

#for student in students:
#    name, number, cca = student
#    print(f"Name : {name}")
#    print(f"Number : {number}")
#    print(f"CCA : {cca}")


#Task 1:
#list1 = ["Apple", "Banana", "Cherry"]
#list2 = ["Durian", "Elderberry", "Figs"]
#listCon = []

#listCon = list1 + list2
#print(listCon)

#Task 2:
#listCon = []
#list1 = [3.20, 2.65, 1.75]
#list2 = [6.15, 5.45, 4.20]

#listCon = list1 + list2
#sorted_listCon = sorted(listCon)
# sorted_listCon = sorted(listCon, reverse = True)
#above if you want reverso
#print(sorted_listCon)

#Task 3:
#abc = []
#otherHalf = []
#fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
#index = 3
#abc = fruits[:index]
#otherHalf = fruits[index:]
#print(abc)
#print(otherHalf)

#Task 4:
#abc = []
#otherHalf = []
#fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
#aVeryNiceFloor = len(fruits) // 2
#abc = fruits[:aVeryNiceFloor]
#otherHalf = fruits[aVeryNiceFloor:]
#print(abc)
#print(otherHalf)

#Task 5:
#hiAgain = [] #common list
#list1 = ["Apple", "Banana", "Cherry", "Durian"]
#list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
#for i in list1:
#    if i in list2:
#        hiAgain.append(i)
#print(hiAgain)

#Task 6:
#unicorn = []
#list1 = ["Apple", "Banana", "Cherry", "Cherry"]
#list2 = ["Cherry", "Durian", "Durian", "Figs"]

#for i in list1:
#    if i not in unicorn:
#        unicorn.append(i)

#for i in list2:
#    if i not in unicorn:
#        unicorn.append(i)
#print(unicorn)

#Task 7:
#allEvenClub = []
#all = []
#list1 = [1, 2, 3, 4]
#list2 = [5, 6, 7, 8]
#all = list1 + list2
#for i in all:
#    if i % 2 == 0:
#        allEvenClub.append(i)
#print(allEvenClub)

#Task 8:
#pancake = []
#nested_list = [[1, 2], [3, 4], [5, 6]]
#for pairs in nested_list:
#    for people in pairs:
#        pancake.append(people)
#print(pancake)

#Task 9:
students = [1, 2, 3, 4, 5, 6, 7, 8, 9]
groups = []
size = 3
for i in range(0, len(students), size):
    groups.append(students[i:i+size])
print(groups)