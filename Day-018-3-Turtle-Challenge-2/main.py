from turtle import Turtle, Screen

raphael = Turtle()
raphael.shape("turtle")
raphael.color("red")

for _ in range(20):
    raphael.pendown()
    raphael.forward(10)
    raphael.penup()
    raphael.forward(10)

screen = Screen()
screen.exitonclick()
