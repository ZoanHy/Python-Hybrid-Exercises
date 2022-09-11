import turtle as t

zoan = t.Turtle()

zoan.shape()


def draw_a_dashed_line():
    for _ in range(5):
        zoan.forward(20)
        zoan.penup()
        zoan.forward(20)
        zoan.pendown()



draw_a_dashed_line()
t.Screen().exitonclick()
