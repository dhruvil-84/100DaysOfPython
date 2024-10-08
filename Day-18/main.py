from turtle import Turtle, Screen
import random

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
# timmy.pensize(15)
# screen.colormode(255)
# timmy.speed("fastest")
# # colours = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red", "Cyan", "Teal", "Pink", "CornflowerBlue",
# #            "DarkOrchid", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "IndianRed", "Wheat", "SeaGreen", "Brown"]

# direction = [0, 90, 180, 270]

# for _ in range(200):
#     # timmy.color(random.choice(colours))
#     timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     timmy.fd(30)
#     timmy.setheading(random.choice(direction))

# Draw a spiral of different colours.
# timmy.speed("fastest")
# for steps in range(100):
#     for c in ("blue", "red", "green"):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)

# Dray a Star.
# timmy.speed("fastest")
# timmy.color('red')
# timmy.fillcolor('yellow')
# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break
# timmy.end_fill()

# Draw a square with .setheading().
# screen.bgcolor("black")
# screen.title("Drawing a square with .setheading()")
# timmy.color("blue", "yellow")
# timmy.pensize(2)
# timmy.begin_fill()
# timmy.forward(100)
# timmy.setheading(90)
# timmy.forward(100)
# timmy.setheading(180)
# timmy.forward(100)
# timmy.setheading(270)
# timmy.forward(100)
# timmy.setheading(0)
# timmy.end_fill()
# txt = screen.textinput("NIM", "Name of first player:")
# timmy.write(txt)

# Draw a spirograph.
timmy.speed("fastest")
screen.colormode(255)

for i in range(int(360 / 5)):
    rotation = timmy.heading()
    timmy.color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    timmy.circle(100)
    timmy.setheading(rotation + 5)

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
    13. .heading()
    14. .speed()
    15. .begin_fill() and .end_fill()
    16. .dot(size, colour)
    17. .showturtle()
    18. .hideturtle()
    19. .isinvisible()
    20. .teleport()
    
methods of Screen class:
    1. .exitonclick()
    2. .colormode(255)
    3. .bgcolor()
    4. .title()
    5. .textinput("title", "question")
    6. .canvwidth()
    7. .canvheight()
    8. .cleascreen() / .clear()
"""