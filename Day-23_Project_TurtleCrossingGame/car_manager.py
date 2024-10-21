# Importing all the modules required.
import random
from turtle import Turtle

# Defining the constants.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POS = [-260, -220, -180, -140, -100, -60, -20, 20, 40, 80, 120, 160, 200, 240, 260]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """creation and addition of the car in the car array"""
        mode = [1, 3, 4, 6]
        random_chance = random.randint(1, 6)
        if random_chance in mode:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=0.7, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=random.choice(Y_POS))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        """continuously moving a car"""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        """increasing the speed of car if level increases"""
        self.car_speed += MOVE_INCREMENT
