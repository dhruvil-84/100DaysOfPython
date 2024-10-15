from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.shapesize()
        self.penup()
        self.timer = 0.07
        self.x_move = random.choice((10, -10))
        self.y_move = random.choice((10, -10))
        self.rapid_reflection_permission = True # This is not working!! (BUG)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))
        self.rapid_reflection_permission = True

    def bounce(self):
        self.y_move *= -1

    def reflect(self):
        if self.rapid_reflection_permission:
            self.x_move *= -1
            self.increase_speed()
        self.rapid_reflection_permission = False

    def movement(self):
        self.x_move = random.choice((10, -10))
        self.y_move = random.choice((10, -10))

    def increase_speed(self):
        if self.timer > 0.03:
            self.timer -= 0.01

    def reset_position(self):
        self.goto(0,0)
        self.timer = 0.07
        self.movement()
        # self.goto((480, 288))
        # self.goto((480, -280))
        # self.goto((-488, 288))
        # self.goto((-488, -280))
