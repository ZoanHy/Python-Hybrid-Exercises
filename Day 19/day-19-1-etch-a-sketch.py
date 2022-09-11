from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(50)


def move_backward():
    tim.backward(50)


def counter_clockwise():
    tim.setheading(tim.heading() + 10)


def clockwise():
    tim.setheading(tim.heading() - 10)


def clear_monitor():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_monitor)

screen.exitonclick()
