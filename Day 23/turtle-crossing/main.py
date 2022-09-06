import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

zoan = Player()

turtle.listen()
turtle.onkey(key="Up", fun=zoan.move_up)

car_manager = CarManager()
car_manager.create_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()

    for car in car_manager.cars:
        car_manager.move_car(car)


