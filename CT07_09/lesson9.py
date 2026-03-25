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
import turtle
#Global Variables
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()
#Functions
def draw_square():
    t.seth(0)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)
#Main Code:
t.speed(0)
t.penup()

draw_square()
t.forward(100)
draw_square()

turtle.done()