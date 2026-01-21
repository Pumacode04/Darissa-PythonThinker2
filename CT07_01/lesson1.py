# print("Hello from lesson 1")

# Recap 1

#1. check what material the item is.
#2. if the item is made out of glass, put it in the glass bin.
#3. if the item is made out of plastic, put it in the plastic bin.
#4. if the item is made out of paper, put it in the paper bin.
#5. repeat the above till everything is sorted out.

#str(100)

# Recap 2

# red = 1 * 3
# blue = 2 * 5
# green = 3 * 4
# print("Your total is : $" + str(red + blue + green))

# Recap 3

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))

score = input("What is your score.")
if int(score) >= 75:
    print("A")
elif int(score) >= 60:
    print("B")
elif int(score) >= 50:
    print("C")
else :
    print("Fail")