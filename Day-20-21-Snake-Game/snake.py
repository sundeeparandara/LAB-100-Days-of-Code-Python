from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
INCREMENTS = 20

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
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)