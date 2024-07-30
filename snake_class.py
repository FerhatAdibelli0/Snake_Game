import random
from turtle import Turtle

SEGMENT_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
DISTANCE = 20
RIGHT = 0
UP = 90
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in SEGMENT_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        my_turtle = Turtle("square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(position)
        self.turtles.append(my_turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[index - 1].xcor()
            new_y = self.turtles[index - 1].ycor()
            self.turtles[index].goto(new_x, new_y)

        self.head.forward(DISTANCE)

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
