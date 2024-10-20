# Importing all the modules required.
from turtle import Turtle

# Defining the constants.
ALIGNMENT = "center"
FONT = ('Courier', 17, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(x = 0, y = 270)
        self.print_score(score = self.score)
        self.hideturtle()

    def increase_score(self):
        """increases the current score by 1 when a snake consumes an apple"""
        self.score += 1
        self.clear()
        self.print_score(score = self.score)

    def game_over(self):
        """prints game over on the screen if a snake collides with its body or on the wall"""
        self.goto(x = 0, y = 0)
        self.color("Black")
        self.write(f"Game Over", align = ALIGNMENT, font = ('Courier', 17, 'bold'))
        # you can use tkinter here to display game over and ask for replay with two buttons yes or no and return its true or false value in main.py to make further steps.

    def print_score(self, score):
        """prints the score at the score board"""
        self.write(f"Score : {score}", align = ALIGNMENT, font = FONT)
