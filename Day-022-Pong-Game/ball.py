from turtle import Turtle
import time
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_increment = 10#*random.uniform(0,3)
        self.y_increment = 10#*random.uniform(0,3)
        self.ball_speed = 1


    def move(self):
        time.sleep(0.1 / self.ball_speed)
        new_x = self.xcor() + self.x_increment
        new_y = self.ycor() + self.y_increment
        self.goto(new_x,new_y)
        print(f"Ball position: {self.position()}")

    def wall_bounce(self):
        self.y_increment *= -1

    def paddle_bounce(self):
        self.x_increment *= -1
        self.ball_speed += 0.5

    def reset_ball(self):
        time.sleep(1)
        self.ball_speed = 1
        self.goto(0,0)
        self.x_increment *= -1


