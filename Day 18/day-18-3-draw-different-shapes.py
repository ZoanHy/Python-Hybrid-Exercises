import turtle as t
import random as r

zoan = t.Turtle()


def random_color():
    R = r.random()
    B = r.random()
    G = r.random()
    global zoan
    zoan.color(R, G, B)


def draw_different_shapes():
    for edge in range(3, 11):
        random_color()
        for i in range(edge):
            zoan.forward(70)
            zoan.right(360 / edge)



draw_different_shapes()

t.Screen().exitonclick()
