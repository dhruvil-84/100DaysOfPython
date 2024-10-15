from turtle import Turtle

class Partition(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.teleport(x=0, y=280)
        self.setheading(270)
        for i in range((280 - -280) // 20):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.hideturtle()
