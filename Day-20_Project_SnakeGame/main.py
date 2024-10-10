import turtle
import time
from snake import Snake

screen = turtle.Screen()
screen.setup(width = 600, height = 600)
screen.listen()
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0) # turning tracer method off (i.e. setting it 0). Turn turtle(snake_body) animation off.

snake = Snake()

game = True
while game:
    screen.update() # updating the screen only after my snake moves (i.e. not showing the single body of snake moving)
    time.sleep(0.1) # Adding Delay so I can see the snake moving.
    screen.onkey(key = "Up", fun = snake.move_up)
    screen.onkey(key = "Down", fun = snake.move_down)
    screen.onkey(key = "Right", fun = snake.move_right)
    screen.onkey(key = "Left", fun = snake.move_left)
    snake.move()
    # code of game over, score and food is in Day-21........

screen.exitonclick()