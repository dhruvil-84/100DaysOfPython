from turtle import Turtle

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
        self.score += 1
        self.clear()
        self.print_score(score = self.score)

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.color("Black")
        self.write(f"Game Over", align = ALIGNMENT, font = ('Courier', 17, 'bold'))

    def print_score(self, score):
        self.write(f"Score : {score}", align = ALIGNMENT, font = FONT)
