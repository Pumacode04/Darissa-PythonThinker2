# print("Hello from lesson 9")

#Recap 1:
#correct = False
#answer = input("What has to be broken before you can use it? ")
#answer = answer.lower()
#if "egg" in answer:
#    correct = True
#if correct:
#    print("Good.")
#else:
#    print("Try Again.")

#Task 1:
#Import Libraries
#import turtle
#Global Variables
#screen = turtle.Screen()
#t = turtle.Turtle()
#t.speed(0)
#t.penup()
#Functions
#def draw_square():
#    t.seth(0)
#    t.pendown()
#    for i in range(4):
#        t.forward(50)
#        t.right(90)
#Main Code:
#t.speed(0)
#t.penup()

#t.goto(-200, 200)
#for i in range(6):
#    draw_square()
#    t.penup()
#    t.forward(60)

#t.goto(-140, 140)
#for i in range(4):
#    draw_square()
#    t.penup()
#    t.forward(60)

#Task 2:
#t.goto(-80, 80)
#for i in range(2):
#    draw_square()
#    t.penup()
#    t.forward(60)

# # 1. Import Libraries
# import turtle

# # 2. Global Variables
# screen = turtle.Screen()
# t = turtle.Turtle()

# # 3. Functions
# def draw_square(size):
#     t.seth(0)
#     t.pendown()
#     for i in range(4):
#         t.forward(size)
#         t.right(90)

# # 4. Main Code
# t.speed(0)

# for size in range(50, 400, 50):
#     t.penup()
#     t.goto(-size / 2, size / 2)
#     draw_square(size)

# turtle.done()

#Task 3:
#Import Libraries
#import turtle
#Global Variables
#screen = turtle.Screen()
#t = turtle.Turtle()
#t.speed(0)
#t.penup()
#Functions
#Functions
#def draw_shape(length, sides):
#    t.seth(180)
#    t.pendown()
#    for i in range(sides):
#        t.forward(length)
#        t.right(360/sides)

#length = input("Length : ")
#sides = input("Sides : ")
#t.speed(0)
#t.penup()
#draw_shape(int(length), int(sides))
#or
#length = int(screen.textinput("Length", "Enter length"))
#sides = int(screen.textinput("Number of sides", "Enter number of sides"))

#Task 4:
#Import Libraries
import turtle
#Global Variables
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
#Functions
def draw_square():
    t.seth(180)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)
def draw_triangle():
    t.seth(180)
    t.pendown()
    for i in range(3):
        t.forward(100)
        t.right(120)
#Main code:
t.speed(0)
t.penup()
draw_square()
t.goto(0, 100)
draw_triangle()

turtle.done()