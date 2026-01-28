#print("Hello from lesson 3")
import time
import random


#Task 1, probably??? :
#import time

#print("hello.")
#time.sleep(1)
#print("you're boring. bye bye.")

#actual task 1, trust :
#import time

#studytime = input("how many minutes you wanna study?")
#studytime = float(studytime) * 60
#for i in range(int(studytime), -1, -1):
#    print(i)
#    time.sleep(1)

#task 2:
#savings = 0
#dailySavings = ""
#while savings < 100:
#    dailySavings = input("hey, how much you save today ah?\n")
#    savings = savings + int(dailySavings)
#    print("you have ONLY saved $" + str(savings) + ".")
#print("congratulations?")
firstNum = 0
secondNum = 0
score = 0
answer = ""
chance = 3
firstNum = random.randint(2, 100)
secondNum = random.randint(2,100)

while score != 15:
    answer = input(str(firstNum) + "x" + str(secondNum) + " = ")
    if int(answer) == firstNum * secondNum:
        score += 1
        firstNum = random.randint(2, 100)
        secondNum = random.randint(2,100)
    elif int(answer) != firstNum * secondNum:
        chance -= 1
        print("try again.")
        print("oh yeah, reminder : you have " + str(chance) + " tries left haha...")
    if chance == 0:
        print("go to remedial lessons.")
        break
    print("current score : " + str(score))
if score == 15:
    print("oh. good job.")