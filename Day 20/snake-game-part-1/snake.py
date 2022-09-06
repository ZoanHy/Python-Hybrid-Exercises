from turtle import Turtle

NUM_START_PART = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_part = []
        self.create_snake()
        self.head = self.snake_part[0]

    def create_snake(self):
        for i in range(0, NUM_START_PART):
            new_part = Turtle(shape="square")
            new_part.color("white")
            new_part.penup()
            if i != 0:
                x_prev = self.snake_part[i - 1].position()[0]
                y_prev = self.snake_part[i - 1].position()[1]
                new_part.setposition(x_prev - 20, y_prev)
            self.snake_part.append(new_part)

    def move(self):
        # for part_num in range(start=2, stop=0, step=-1):
        for part_num in range(len(self.snake_part) - 1, 0, -1):
            new_x = self.snake_part[part_num - 1].xcor()
            new_y = self.snake_part[part_num - 1].ycor()
            self.snake_part[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
