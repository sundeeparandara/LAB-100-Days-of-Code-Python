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

        #print(f"snake is {len(self.segments)} segment long")

    def move(self):
        for segment_id in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[segment_id - 1].xcor()
            new_y = self.segments[segment_id - 1].ycor()
            self.segments[segment_id].goto(new_x, new_y)
        self.segments[0].forward(INCREMENTS)