from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="f", fun=move_forwards)

screen.exitonclick()

