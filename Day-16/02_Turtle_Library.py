# about turtle library - docs.python.org/3/library/turtle.html
"""
import turtle
timmy = turtle.Turtle() # accessing Turtle class from turtle module and actually constructing an object named timmy.
                                                       OR
"""
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
print(type(timmy))
timmy.shape("turtle")
timmy.color("teal")
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.backward(200)
timmy.right(90)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) # By Default canvheight = 300
print(my_screen.canvwidth) # By Default canvwidth = 400

my_screen.exitonclick()