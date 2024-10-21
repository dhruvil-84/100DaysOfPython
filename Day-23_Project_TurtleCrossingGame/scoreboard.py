# Importing all the modules required.
from turtle import Turtle

# Defining the constants.
FONT = ("Courier", 20, "bold")
ALIGN = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-145, 263)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_level(self):
        """increases the level by 1 when the player crosses to other side."""
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        """prints GAME OVER on the screen if player collides with the car."""
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGN, font=FONT)
