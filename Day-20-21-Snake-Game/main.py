from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_length = 3
x_pos = 0
x_head = 0
y_pos = 0
block_increment = 20
snake = []

for _ in range(snake_length):
    square = Turtle("square")
    square.penup()
    square.speed("fastest")
    square.goto(x=x_pos, y=0)
    square.color("white")
    snake.append(square)
    x_pos -= 20


for i in range(10):
    x_head = block_increment*i
    x_pos = x_head
    j = 1
    print(f"round {i}")
    for square in snake:
        square.goto(x_pos,y=0)
        position = square.pos()
        print(f"{j} : {position}")
        j +=1
        x_pos -= 20

# for i in range(10):
#     x_head = block_increment*i
#     x_pos = x_head
#     print(x_pos)
#     for _ in range(snake_length):
#         square = Turtle("square")
#         square.penup()
#         square.color("white")
#         square.goto(x=x_pos,y=0)
#         x_pos -= 20

















screen.exitonclick()