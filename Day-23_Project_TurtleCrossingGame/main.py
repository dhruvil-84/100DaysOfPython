import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=450, height=600)
screen.bgcolor("Black")
screen.bgpic("hop_mania.png")
screen.title("Hop Mania")
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)

game = True
while game:
    time.sleep(0.1)
    screen.update()
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