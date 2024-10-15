from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() <= 230:
            x = self.xcor()
            y = self.ycor()
            y += 20
            self.goto(x, y)

    def move_down(self):
        if self.ycor() >= -230:
            x = self.xcor()
            y = self.ycor()
            y -= 20
            self.goto(x, y)
