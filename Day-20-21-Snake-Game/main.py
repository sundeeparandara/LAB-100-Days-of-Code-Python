from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

square = Turtle("square")
square.fillcolor("white")

snake_length = 3
x_pos = 0

for i in range(snake_length):
    square = Turtle("square")
    square.penup()
    square.color("white")
    square.goto(x=x_pos,y=0)
    x_pos -= 20

snake = []















screen.exitonclick()