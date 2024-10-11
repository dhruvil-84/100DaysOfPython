import turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = turtle.Screen()
screen.setup(width = 600, height = 600)
screen.listen()
screen.bgcolor("Black")
screen.bgpic("green_field.png")
screen.title("Snake Move")
screen.tracer(0) # turning tracer method off (i.e. setting it 0). Turn turtle(snake_body) animation off.

snake = Snake()
food = Food()
score = Score()

# actions to be performed after the responses taken from the user through keyboard.
screen.onkey(key = "Up", fun = snake.move_up)
screen.onkey(key = "Down", fun = snake.move_down)
screen.onkey(key = "Right", fun = snake.move_right)
screen.onkey(key = "Left", fun = snake.move_left)

game = True
while game:
    screen.update() # updating the screen only after my snake moves (i.e. not showing the single body of snake moving)
    time.sleep(0.1) # Adding Delay so I can see the snake moving.
    snake.move()

    # Detect collision with food.
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 270 or snake.snake_head.ycor() < -280:
        score.game_over()
        game = False

    # Detect collision with body.
    for body in snake.snake[1:]:
        if snake.snake_head.distance(body) < 10:
            score.game_over()
            game = False

screen.exitonclick()

# print in the collision with body and wall so i know where is that one bug!!.
# apple image.
# ask for replay.