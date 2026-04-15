#print("Hello from lesson 11")
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()

screen.bgcolor("forest green")
width = screen.window_width()
height = screen.window_height()
#print(width, height)

t.shape("square")
t.penup()
t.goto(-width / 2 + 20, height / 2 - 100)

for i in range(int(-width / 2 + 10) , int(width / 2 - 10), 30):
    t.setx(i)
    t.stamp()

t.goto(-width / 2, -height / 2 + 100)
t.pencolor("red")
t.pendown()
t.goto(width / 2, -height / 2 + 100)

#1st contestant
Pink_square = turtle.Turtle()

Pink_square.penup()

Pink_square.shape("square")
Pink_square.color(1, 0.4, 0.7)
Pink_square.goto(0, -height / 2 + 100)
Pink_square.seth(90)
Pink_square.write("Square", align="center", font=("Arial", 15))

#2nd contestant
Blue_triangle = turtle.Turtle()

Blue_triangle.penup()

Blue_triangle.shape("triangle")
Blue_triangle.color(0, 0, 1)
Blue_triangle.goto(width / 4, -height / 2 + 100)
Blue_triangle.seth(90)
Blue_triangle.write("Triangle", align="center", font=("Arial", 15))

#3rd contestant
green_turtle = turtle.Turtle()

green_turtle.penup()

green_turtle.shape("turtle")
green_turtle.color(0.2, 1, 0.2)
green_turtle.goto(-width / 4, -height / 2 + 100)
green_turtle.seth(90)
green_turtle.write("Turtle", align="center", font=("Arial", 15))

#Enter your guess:
guess = input("Guess: ")

#RACE STARTS NOW!
contestants = [Pink_square, Blue_triangle, green_turtle]
race_end = False
while not race_end:
    for i in range(len(contestants)):
        contestants[i].pendown()
        contestants[i].seth(random.randint(75, 115))
        contestants[i].forward(random.randint(1, 20))

        if contestants[i].ycor() > height / 2 - 100:
            if i == 0:
                winner = "Pink_square"
            elif i == 1:
                winner = "Blue_triangle"
            else:
                winner = "green_turtle"
            print(f"Winner: {winner}")
            race_end = True

if guess.lower == winner.lower():
    print("Your guess is correct!")
else:
    print("Your guess is wrong!")

turtle.done()