import turtle
import time
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from partition import Partition

screen = turtle.Screen()
screen.setup(width=1000, height=660)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

def pong():
    left_paddle = Paddle((-450, 0))
    right_paddle = Paddle((450, 0))

    player1_name = screen.textinput("Player1 Name", "Enter Player 1's Name:")
    player2_name = screen.textinput("Player2 Name", "Enter Player 2's Name:")
    screen.listen()

    player1 = Scoreboard(player_name=player1_name, x_units=-250, y_units=300)
    player2 = Scoreboard(player_name=player2_name, x_units=250, y_units=300)

    ball = Ball()
    partition = Partition()

    screen.onkeypress(key="Up", fun=right_paddle.move_up)
    screen.onkeypress(key="Down", fun=right_paddle.move_down)
    screen.onkeypress(key="w", fun=left_paddle.move_up)
    screen.onkeypress(key="s", fun=left_paddle.move_down)

    while player1.score != 5 and player2.score != 5:
        time.sleep(ball.timer)
        screen.update()
        ball.move()

        # Detect collision of ball at top and bottom.
        if ball.ycor() <= -280 or ball.ycor() >= 280:
            ball.bounce()

        # Detect collision of ball with paddle. (BUG HERE)
        if (ball.distance(left_paddle) <= 50 and -430 >= ball.xcor() >= -450) or (ball.distance(right_paddle) <= 50 and 430 <= ball.xcor() <= 450):
            ball.reflect()
            # change colour to opposite player's colour.

        # Detect if ball does not hit the right paddle.
        if ball.xcor() > 510:
            ball.reset_position()
            player1.increase_score()

        # Detect if ball does not hit the left paddle.
        if ball.xcor() < -510:
            ball.reset_position()
            player2.increase_score()

pong()

screen.exitonclick()

# add background image and borders or boundary.
# add strictness that if ball passes hits player's paddle then it cannot move until the ball hits other player's paddle or miss by other player.

# paddle colour left and cyan blue and the ball colour changes of it reflects red then colour changes to blue and if it reflects blue then changes to red. (Initially ball colour must be white/yellow)
# score should also be in colour.
# before starting display Press space/enter to start.
# instead of score of player1 and score of player2, I need name of players (use textinput of turtle). NOTE while asking player1 name's colour must be same as left bar and player2's name colour as right bar.
# At last show which player wins.
# Add doc strings and comments.
# after learning tkinter ask for play again.
