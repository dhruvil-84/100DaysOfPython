from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 17, 'normal')

class Scoreboard(Turtle):
    def __init__(self, player_name, x_units, y_units):
        super().__init__()
        self.score = 0
        self.name = player_name
        self.color("White")
        self.penup()
        self.goto(x=x_units, y=y_units)
        self.print_score()
        self.hideturtle()

    def print_score(self):
        self.write(f"{self.name}'s Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()