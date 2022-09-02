# import turtle
# tim = turtle.Turtle()

from turtle import Turtle, Screen
tim = Turtle()

import heroes
print(heroes.gen())

import turtle as t
tim = t.Turtle()
#####Turtle Intro######



# timmy_the_turtle = Turtle()
#
# # screen = Screen()
#
# # screen.exitonclick()
#
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(180)
# timmy_the_turtle.forward(100)
#
# turtle.Screen().exitonclick()

######## Challenge 1 - Draw a Square ############

def draw_a_square():
    global zoan_tt
    for _ in range(4):
        zoan_tt.right(90)
        zoan_tt.forward(100)


zoan_tt = Turtle()
zoan_tt.shape("turtle")
zoan_tt.color("green")
draw_a_square()

turtle.Screen().exitonclick()
