# Importing all the modules required.
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = self.getscreen() # Getting the screen of main.py and storing that in screen variable.
        self.screen.register_shape("apple.gif")  # Register the image as a shape.
        self.shape("apple.gif")  # Set the shape to the apple image.
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """refreshes the position of apple"""
        self.goto(x = random.randint(-280, 280), y = random.randint(-280, 260))
