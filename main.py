import turtle

import random

window = turtle.Screen()
window.bgcolor("sky blue")

fred = turtle.Turtle()
fred.color("red")
fred.shape("turtle")
fred.penup()
fred.setx(90)
fred.sety(-90)
fred.left(90)

amy = turtle.Turtle()
amy.color("orange")
amy.shape("turtle")
amy.penup()
amy.setx(-90)
amy.sety(-90)
amy.left(90)

line = turtle.Turtle()
line.penup()
line.setx(-100)
line.sety(200)
line.pendown()
line.forward(250)
line.hideturtle()



def start():
    start = True

    while start:

        fred.forward(random.randint(1, 5))
        amy.forward(random.randint(1, 5))

        if fred.ycor() >= 200:
            fred.color("green")
            start = False
        if fred.ycor() >= 200:
            fred.color("green")
            start = False

window.onkeypress(start, "space")
window.listen()


