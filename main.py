import turtle as turtle
import colorgram
import random as rnd


def set_starting_position():
    t.penup()
    t.goto(-250, -250)


def start_new_row():
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(-500)


def paint_row():
    t.dot(20, rnd.choice(rgb_colors))
    t.forward(50)


colors = colorgram.extract("painting.jpg", 100)

rgb_colors = []

for c in colors:
    rgb_colors.append(tuple(c.rgb))

turtle.colormode(255)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

set_starting_position()
i = 0
while i < 10:
    for j in range(10):
        t.dot(20, rnd.choice(rgb_colors))
        t.forward(50)
    start_new_row()
    i += 1

screen = turtle.Screen()
screen.exitonclick()
