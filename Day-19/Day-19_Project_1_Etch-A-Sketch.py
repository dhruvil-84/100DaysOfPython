import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()
screen.listen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_right():
    timmy.right(10)

def turn_left():
    timmy.left(10)

def clr_scr():
    screen.reset()

screen.onkey(fun = move_forward, key = "w")
screen.onkey(fun = move_backward, key = "s")
screen.onkey(fun = turn_right, key = "d")
screen.onkey(fun = turn_left, key = "a")
screen.onkey(fun = clr_scr, key = "c")

screen.exitonclick()