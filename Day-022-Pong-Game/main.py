from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import random
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")



game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    #upper and lower wall collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.wall_bounce()

    #right or right paddle collision detection
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.paddle_bounce()

    #out of bounds - right
    if (ball.xcor()>380):
        print("out of bounds - right")
        ball.reset_ball()

    # out of bounds - left
    if (ball.xcor()<-380):
        print("out of bounds - left")
        ball.reset_ball()






screen.exitonclick()