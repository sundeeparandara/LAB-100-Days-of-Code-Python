from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed("fastest")
#turtle.width(10)

for angle in range(0,360,10):
    turtle.setheading(angle)
    turtle.circle(100)

screen = Screen()
screen.exitonclick()