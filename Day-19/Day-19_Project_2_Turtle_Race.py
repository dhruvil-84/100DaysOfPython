import turtle
import random

screen = turtle.Screen()
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:").lower()

t=[]
colours = ["purple", "blue", "green", "yellow", "orange", "red"]
y_cord = -150
for i in range(0, 6):
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x = -300, y = y_cord)
    t.append(new_turtle)
    y_cord += 50

race = True
while race:
    for turtles in t:
        turtles.forward(random.randint(0, 10))
        if turtles.xcor() >= 300:
            race = False
            winner = turtles.pencolor()
            if user_bet == winner:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've Lost! The {winner} turtle is the winner!")
            break
screen.exitonclick()