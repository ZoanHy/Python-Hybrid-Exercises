import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########
zoan = t.Turtle()
zoan.speed("fastest")


# def spiro_graph():
#     for corner in range(0, 361, 5):
#         zoan.color(random_color())
#         zoan.circle(100)
#         zoan.setheading(corner)

def spiro_graph_v2(gap_of_size):
    for _ in range(int(360 / gap_of_size)):
        zoan.color(random_color())
        zoan.circle(100)
        zoan.setheading(zoan.heading() + gap_of_size)


spiro_graph_v2(10)

# spiro_graph()

t.Screen().exitonclick()
