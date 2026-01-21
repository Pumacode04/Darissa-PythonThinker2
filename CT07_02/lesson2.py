# print("Hello from lesson 2")

#just a task below

#for i in range(1, 13+1, 2):
#    print(i)

#recap 1
#for i in range(0, 21):
#    print(i)

#for i in range(1, 31):
#    print(i)

#for i in range(2, 25, 2):
#    print(i)


#Task 1
#counter = 0
#while counter < 21:
#    print(counter)
#    counter += 1

#counter = 1
#while counter < 31:
#    print(counter)
#    counter += 1

#counter = 2
#while counter < 25:
#    print(counter)
#    counter += 2


#Task 2:

#import time

#num = 10
#while num != 0:
#    print(num)
#    time.sleep(1)
#    num -= 1
#else:
#    print("Happy New Year!")

#num = 10
#while num != 0 :
#    print(num)
#    num -= 1
#    if num == 5 :
#        break
#else :
#    print("Happy New Year")

#Task 3

#count = 1
#while count != 11:
#    print(count)
#    count += 1
#else:
#    print("Variable count has reached ten for your infomation.") 

#Task 4:

#haha = ""
#toppings = ""
#while haha != "no":
#    haha = input("anything you would want in your pizza.")
#    if haha == "no":
#        break
#    toppings = haha + " " + toppings
#print(toppings)

#Task 5:
#import time

#answer = ""
#score = 0
#while score != 1:
#    answer = input("Can a chicken fly long distance?")
#    if answer == "no":
#        score += 1
#        print("okay, next question.")
#    else:
#        print("haha, wrong. try again.")

#while score != 2:    
#    answer = input("true or false : are water droplets blue?")
#    if answer == "no":
#        score += 1
#        print("okay, last question.")
#    else :
#        print("try again, haha.")

#while score != 3:
#    answer = input("Is wood flexible? (the ability to bend without breaking)")
#    if answer == "no":
#        score += 1
#        print("you completed the test.")
#    else:
#        print("wow, you got it correct!")
#        time.sleep(1)
#        print("nah, Try Again.")
#print("oh, you won. congrats?")
#time.sleep(1)
#print("they're just common sense questions.")


# text = "ABC"
# text = text.lower() # "abc"

#21st of January, 2026
#Task 5 (bonus) :
import time

answer = ""
score = 0
chance = 3
points = 0

while score != 1:
    answer = input("Can a chicken fly long distance?\n")
    if answer == "no":
        chance = 3
        score += 1
        points += 15
        print("okay, next question.")
    else:
        print("haha, wrong. try again.")
        chance -= 1
        points -= 5
        if chance == 0:
            print("bye bye. you failed.")
            break

print("you have " + str(points) + " points.")

while score != 2 and chance != 0:    
    answer = input("true or false : are water droplets blue?\n")
    if answer == "no":
        chance = 3
        score += 1
        points += 15
        print("okay, last question.")
    else :
        print("try again, haha.")
        chance -= 1
        points -= 5
        if chance == 0:
            print("haha. you failed.")
            break

print("you have " + str(points) + " points")

while score != 3 and chance != 0:
    answer = input("Is wood flexible? (the ability to bend without breaking)\n")
    if answer == "no":
        score += 1
        points += 15
        print("you completed the test.")
    else:
        print("wow, you got it correct!")
        time.sleep(1)
        print("nah, Try Again.")
        chance -= 1
        points -= 5
        if chance == 0:
            print("too bad so sad. bye.")
            break

if chance != 0:
    print("you have " + str(points) + " points. although they hold no meaning.")
    print("oh, you won. congrats?")
    time.sleep(1)
    print("they're just common sense questions.")
