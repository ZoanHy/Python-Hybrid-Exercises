from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_random = random.randint(-250, 250)
            new_car.goto(300, y_random)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.cars_speed)

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT
