import turtle as t
import random

zoan = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]


def random_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return (R, G, B)

zoan.pensize(10)
zoan.speed('fastest')


def random_walk():
    for _ in range(2000):
        # corner = random.choice([-90, 90])
        # zoan.right(corner)
        zoan.color(random_color())
        zoan.forward(50)
        zoan.setheading(random.choice(directions))


random_walk()
t.Screen().exitonclick()
