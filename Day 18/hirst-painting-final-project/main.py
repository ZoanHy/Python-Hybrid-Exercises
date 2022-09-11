import random
import turtle as t
import random as r

import colorgram

colors_extract = colorgram.extract('hirst-dot.jpg', 12)

colors = []
for color in colors_extract:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    colors.append((red, green, blue))

colors_list = [(240, 239, 237), (237, 231, 234), (231, 239, 234), (224, 232, 237), (236, 34, 108), (150, 26, 64),
               (240, 74, 34), (7, 148, 93), (224, 169, 43), (180, 159, 46), (27, 125, 192), (43, 191, 232)]

t.colormode(255)


# zoan.speed("fastest")

def hirst_painting():
    zoan = t.Turtle()
    zoan.setheading(0)
    zoan.hideturtle()
    zoan.penup()
    zoan.setpos(-250, -250)
    zoan.speed("fastest")
    for dot_count in range(1, 101):
        zoan.dot(20, random.choice(colors_list))
        zoan.forward(50)

        if dot_count % 10 == 0:
            zoan.setheading(90)
            zoan.forward(50)
            zoan.setheading(180)
            zoan.forward(500)
            zoan.setheading(0)


hirst_painting()
t.Screen().exitonclick()
