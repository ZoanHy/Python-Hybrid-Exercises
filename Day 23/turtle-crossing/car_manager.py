from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.penup()
        self.hideturtle()

    def create_car(self):
        make_car = []
        random_y = random.randint(-280, 280)
        random_x = random.randint(-280, 280)
        random_color = random.choice(COLORS)
        for i in range(3):
            new_part = Turtle(shape="square")
            new_part.penup()
            new_part.color(random_color)
            if i != 0:
                new_x = make_car[i - 1].xcor()
                new_y = make_car[i - 1].ycor()

                new_part.goto(new_x - 20, new_y)
            else:
                new_part.goto(random_x, random_y)
            make_car.append(new_part)
        return make_car

    def create_cars(self):
        for i in range(5):
            self.cars.append(self.create_car())

    def move_car(self, car_parts):
        for i in range(len(car_parts) - 1, 0, -1):
            new_x = car_parts[i - 1].xcor()
            new_y = car_parts[i - 1].ycor()
            car_parts[i].goto(new_x, new_y)
        car_parts[0].forward(-20)
