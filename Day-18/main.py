from turtle import Turtle, Screen
from random import choice as r

screen = Screen()
timmy = Turtle()
timmy.shape("arrow")
# timmy.pencolor("grey")
# timmy.fillcolor("black")
timmy.color("grey", "black")

#  Draw a Square:
# for _ in range(4):
#     timmy.fd(100)
#     timmy.left(90)

# Draw a Dashed Line:
# for _ in range(15):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

# Draw a triangle, square, hexagon, heptagon, octagon, nonagon and decagon.
# colours = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red", "Cyan", "Teal", "Pink", "CornflowerBlue",
#            "DarkOrchid", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "IndianRed", "Wheat", "SeaGreen", "Brown"]
# for i in range(3, 11):
#     # outer_angle = 180 - (180 * (i - 2) / i)
#     timmy.color(r(colours))
#     inner_angle = 360 / i
#     for j in range(i):
#         timmy.fd(100)
#         # timmy.right(outer_angle)
#         timmy.right(inner_angle)

# Draw a random walk.
timmy.pensize(15)
timmy.speed("fastest")
colours = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red", "Cyan", "Teal", "Pink", "CornflowerBlue",
           "DarkOrchid", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "IndianRed", "Wheat", "SeaGreen", "Brown"]
direction = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(r(colours))
    timmy.fd(30)
    timmy.setheading(r(direction))
screen.exitonclick()

"""
Classes:
    1. Turtle
    2. Screen
    
methods of Turtle class:
    01. .shape()
    02. .color()
    03. .pencolor()
    04. .fillcolor()
    05. .forward(units) / .fd(units)
    06. .backward(units) / .back(units)
    07. .left(angle)
    08. .right(angle)
    09. .penup()
    10. .pendown()
    11. .pensize()
    12. .setheading()
    13. .speed()
    
methods of Screen class:
    1. exitonclick()
    2. .canvwidth()
    3. .canvheight()
    4. .cleascreen() / .clear()
    5. .bgcolor()
"""