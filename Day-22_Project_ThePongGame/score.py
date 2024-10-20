# Importing all the modules required.
from turtle import Turtle

# Defining the constants.
ALIGNMENT = "center"
FONT1 = ('Courier', 17, 'normal')
FONT2 = ('Courier', 40, 'bold')

class Scoreboard(Turtle):
    def __init__(self, player_name, x_units, y_units, colour):
        super().__init__()
        self.score = 0
        self.name = player_name
        self.color(colour)
        self.penup()
        self.goto(x=x_units, y=y_units)
        self.print_score()
        self.hideturtle()

    def print_score(self):
        """prints the score at the score board"""
        self.write(f"{self.name}'s Score: {self.score}", align=ALIGNMENT, font=FONT1)

    def increase_score(self):
        """increases the player's current score by 1 when an opponent misses to hit the ball"""
        self.score += 1
        self.clear()
        self.print_score()

    def winner(self):
        """prints the winner name on the screen after the game ends"""
        self.setposition(x=0, y=80)
        self.color("Yellow")
        self.write(f"Winner is: {self.name}", align=ALIGNMENT, font=FONT2)
