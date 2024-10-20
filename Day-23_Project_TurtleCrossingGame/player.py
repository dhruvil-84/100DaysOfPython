from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=0.8, stretch_wid=1)
        self.color("purple")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)