from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(),new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")














screen.exitonclick()