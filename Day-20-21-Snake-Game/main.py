from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

length = 3
increment = 20
game_is_on = True
segments = []
snake_starting_positions = [(0,0),(-20,0),(-40,0)]

for pos in snake_starting_positions:
    segment = Turtle("square")
    segment.penup()
    segment.color("white")
    segment.goto(pos)
    segments.append(segment)

screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.5)
    for segment_id in range((len(segments) - 1), 0, -1):
        new_x = segments[segment_id - 1].xcor()
        new_y = segments[segment_id - 1].ycor()
        segments[segment_id].goto(new_x, new_y)
    segments[0].forward(increment)





screen.exitonclick()