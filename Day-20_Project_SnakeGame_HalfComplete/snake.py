import turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0  # EAST
UP = 90    # NORTH
LEFT = 180 # WEST
DOWN = 270 # SOUTH

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            snake_body = turtle.Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(STARTING_POSITION[i])
            self.snake.append(snake_body)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.snake_head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)