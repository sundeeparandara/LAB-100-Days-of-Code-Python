from turtle import Turtle, Screen
import random

mickey = Turtle()
mickey.shape("turtle")
mickey.color("orange")

for sides in range(3, 11):
    angle = 360 / sides
    r = random.randint(0, 255)/255
    g = random.randint(0, 255)/255
    b = random.randint(0, 255)/255
    mickey.pencolor((r, g, b))
    for side in range(0, sides):
        mickey.right(angle)
        mickey.forward(100)



screen = Screen()
screen.exitonclick()