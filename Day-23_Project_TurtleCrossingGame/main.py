# Importing all the modules required.
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=450, height=600) # Setting the screen of dimensions 450 x 600.
screen.bgcolor("Black") # Setting the background color of the screen to black.
screen.bgpic("hop_mania.png") # Creating a field image for the hop mania.
screen.title("Hop Mania")
screen.listen() # Letting the screen listen onclick events generated by the player.
screen.tracer(0) # Turning tracer method off (i.e., setting it 0). Turn turtle(snake_body) animation off.

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

# actions to be performed after the responses taken from the user through the keyboard.
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)

game = True
while game:
    time.sleep(0.1) # Adding Delay so I can see the player moving.
    screen.update() # updating the screen only after plaayer moves (i.e., not showing the animation of player moving)
    car_manager.create_car()
    car_manager.move_car()

    # Detect Collision with the car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game = False
            scoreboard.game_over()

    # Detect if the player reaches to the end.
    if player.ycor() > 280:
        car_manager.level_up()
        player.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()