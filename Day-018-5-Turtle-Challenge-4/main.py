from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed(10)
turtle.width(10)



directions = [0, 90, 180, 270, 360]

turtle.shape("arrow")

for _ in range(100):
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    turtle.pencolor((r, g, b))
    turtle.setheading(random.choice(directions))
    turtle.forward(50)

screen = Screen()
screen.exitonclick()