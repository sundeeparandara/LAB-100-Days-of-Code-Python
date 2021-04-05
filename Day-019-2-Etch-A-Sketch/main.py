from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def forwards():
    turtle.forward(10)

def backwards():
    turtle.backward(10)

def clockwise_bearing():
    turtle.right(10)

def anti_clockwise_bearing():
    turtle.left(10)

def reset_screen():
    turtle.reset()


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise_bearing)
screen.onkey(key="a", fun=anti_clockwise_bearing)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()