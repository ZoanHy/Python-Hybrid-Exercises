import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

zoan = Player()

turtle.listen()
turtle.onkey(key="Up", fun=zoan.move_up)

car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision the car
    for car in car_manager.cars:
        if car.distance(zoan) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect successfull
    if zoan.is_at_finish_line():
        zoan.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()
