import colorgram
import random
import turtle

colours = colorgram.extract("painting.png", 30)

def rgb_val():
    colour = random.choice(colours)
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    tup = (r, g, b)
    return tup

timmy = turtle.Turtle()
turtle.colormode(255)
y = -250
for i in range(10):
    timmy.teleport(-250, y)
    for j in range(10):
        # timmy.pensize(20)
        # timmy.color(rgb_val())
        # timmy.forward(1)
        #  OR
        timmy.dot(20, rgb_val())

        timmy.hideturtle()
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.showturtle()
    y += 50
timmy.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
