from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Red")
        self.penup()
        self.shapesize(stretch_len = 0.75, stretch_wid = 0.75)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x = random.randint(-279, 279), y = random.randint(-279, 270))