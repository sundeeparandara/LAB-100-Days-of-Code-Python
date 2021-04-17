from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()


    def move(self,heading,delay):
        self.setheading(heading)
        self.forward(20)
        time.sleep(delay)
        print(f"Ball position: {self.position()}")


