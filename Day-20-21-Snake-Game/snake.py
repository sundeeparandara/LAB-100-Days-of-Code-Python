from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
INCREMENTS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.increment = 20
        self.segments = []


        for pos in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(pos)
            self.segments.append(segment)

        self.head = self.segments[0]
        #print(f"snake is {len(self.segments)} segment long")

    def move(self):
        for segment_id in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[segment_id - 1].xcor()
            new_y = self.segments[segment_id - 1].ycor()
            self.segments[segment_id].goto(new_x, new_y)
        self.head.forward(INCREMENTS)
        print(self.head.pos())

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

