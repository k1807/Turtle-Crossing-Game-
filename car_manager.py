import random
from turtle import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speeds = MOVE_INCREMENT

    def create_car(self):
        random_ch = random.randint(1,6)
        if random_ch == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speeds)

    def level_up(self):
        self.car_speeds += MOVE_INCREMENT

