# Importing all the modules required.
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, colour):
        super().__init__()
        self.shape("square")
        self.color(colour)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)
        self.make_move = False

    def move_up(self):
        """player's paddle moves up when user hits 'w' or 'Up' arrow key"""
        if self.ycor() <= 230 and self.make_move:
            x = self.xcor()
            y = self.ycor()
            y += 20
            self.goto(x, y)

    def move_down(self):
        """player's paddle moves down when user hits 's' or 'Down' arrow key"""
        if self.ycor() >= -230 and self.make_move:
            x = self.xcor()
            y = self.ycor()
            y -= 20
            self.goto(x, y)

    def can_move(self):
        """giving the permission for player's paddle to move"""
        self.make_move = True

    def cant_move(self):
        """snatching the permission for player's paddle to move"""
        self.make_move = False
