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

zoan = t.Turtle()
zoan.penup()
t.colormode(255)
zoan.speed("fastest")
print(zoan.pos())

zoan.setpos(-200, -250)

def hirst_painting():
    global zoan
    for col in range(10):
        for row in range(10):
            zoan.dot(20, random.choice(colors_list))
            zoan.forward(50)
        zoan.setheading(90)
        zoan.forward(50)
        zoan.setheading(180)
        zoan.forward(500)
        zoan.setheading(0)


hirst_painting()
t.Screen().exitonclick()
