#https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

# import heroes
#
# print(heroes.gen())

screen = Screen()
screen.exitonclick()

