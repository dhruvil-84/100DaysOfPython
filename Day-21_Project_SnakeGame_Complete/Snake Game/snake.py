# Importing all the modules required.
import turtle

# Defining the constants.
STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
RIGHT = 0  # EAST
UP = 90    # NORTH
LEFT = 180 # WEST
DOWN = 270 # SOUTH

# Letting the turtle object to apply colours in rgb() format.
turtle.colormode(255)

def register_body_shape():
    """creating a blunt square shape and registering it as the turtle shape"""
    body_shape = ((-10, -8), (-8, -10), (8, -10), (10, -8),
                  (10, 8), (8, 10), (-8, 10), (-10, 8))
    turtle.register_shape("rounded_square", body_shape)

class Snake:
    def __init__(self):
        self.snake = []
        register_body_shape()
        self.create_snake()
        self.snake_head = self.snake[0]
        self.snake_head.color((61, 125, 237))
        self.rapid_direction_change_permission = True

    def create_snake(self):
        """just creates the initial snake of 3 segments"""
        for position in STARTING_POSITION:
            self.add_body(position)

    def add_body(self, position):
        """creates and appends the snake's body segments"""
        snake_body = turtle.Turtle("rounded_square")
        snake_body.color((61, 107, 219))
        snake_body.penup()
        snake_body.goto(position)
        self.snake.append(snake_body)

    def extend(self):
        """extends the snake's segment whenever an apple is consumed"""
        self.add_body(self.snake[-1].position())

    def move(self):
        """continuously making the snake move"""
        self.rapid_direction_change_permission = True
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].pos())
        self.snake_head.forward(MOVE_DISTANCE)

    def move_up(self):
        """snake moves up when user hits Up arrow key"""
        if self.rapid_direction_change_permission and self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
            self.rapid_direction_change_permission = False

    def move_down(self):
        """snake moves down when user hits Down arrow key"""
        if self.rapid_direction_change_permission and self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
            self.rapid_direction_change_permission = False

    def move_right(self):
        """snake moves right when user hits Right arrow key"""
        if self.rapid_direction_change_permission and self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
            self.rapid_direction_change_permission = False

    def move_left(self):
        """snake moves left when user hits Left arrow key"""
        if self.rapid_direction_change_permission and self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
            self.rapid_direction_change_permission = False
