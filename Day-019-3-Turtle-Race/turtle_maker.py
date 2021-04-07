from turtle import Turtle

class TurtleMaker:

    def __init__(self,color,x,y):
        self.turtle = Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x,y)

    def move_forward(self,steps):
        self.turtle.forward(steps)

    def check_position(self):
        return self.turtle.pos()

    def get_color(self):
        return self.turtle.fillcolor()