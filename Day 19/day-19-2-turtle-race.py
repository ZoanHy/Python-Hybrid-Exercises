import random
import turtle
from turtle import Turtle, Screen

#### Turtle Coordinate System ####

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_positions = [-70, -40, -10, 20, 50, 80]
print(user_bet)
all_turtles = []

# height = -200
# num_turtle = 0
for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.color()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

screen.exitonclick()
