import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########
def spiro_graph():
    zoan = t.Turtle()
    zoan.speed("fastest")
    for corner in range(0, 361, 5):
        zoan.color(random_color())
        zoan.circle(100)
        zoan.setheading(corner)


spiro_graph()

t.Screen().exitonclick()
