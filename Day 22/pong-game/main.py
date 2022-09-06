import time
import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
turtle.listen()
turtle.onkey(key="Up", fun=paddle_right.up)
turtle.onkey(key="Down", fun=paddle_right.down)

turtle.onkey(key="w", fun=paddle_left.up)
turtle.onkey(key="s", fun=paddle_left.down)

scoreboard = Scoreboard()
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle_right
    if ball.distance(paddle_right) < 60 and ball.xcor() > 320 or ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball go out
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()
screen.exitonclick()
