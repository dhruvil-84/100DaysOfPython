# Importing all the modules required.
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Yellow")
        self.shapesize()
        self.penup()
        self.timer = 0.07
        self.x_move = random.choice((10, -10))
        self.y_move = random.choice((10, -10))

    def move(self):
        """moves the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce(self):
        """bounces the ball when collided with top or bottom boundary"""
        self.y_move *= -1

    def reflect(self, paddle):
        """reflects the ball when collided with either of the paddles"""
        self.x_move *= -1
        self.increase_speed()
        # Calculate the difference in y-coordinates between the ball and the paddle
        y_diff = self.ycor() - paddle.ycor()
        # If the ball hits the top part of the paddle, adjust y_move to make it bounce upwards
        if y_diff > 20:
            self.y_move = abs(self.y_move) # Make sure y_move is positive (upwards)
        elif y_diff < -20:
            self.y_move = -abs(self.y_move) # Make sure y_move is negative (downwards)
        # If the ball hits the middle part, y_move remains unchanged
        # Move the ball slightly away from the paddle after reflection
        if self.x_move > 0:
            self.setx(self.xcor() + 10)
        else:
            self.setx(self.xcor() - 10)

    def movement(self):
        """sets the direction of movement in any of one quadrant"""
        self.x_move = random.choice((10, -10))
        self.y_move = random.choice((10, -10))

    def increase_speed(self):
        """increases the speed of the ball every time when the ball hits the paddle"""
        if self.timer > 0.03:
            self.timer -= 0.01

    def reset_position(self):
        """resets the speed and position of the ball"""
        self.goto(0,0)
        self.timer = 0.07
        self.movement()
