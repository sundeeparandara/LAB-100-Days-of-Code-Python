from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_length = 3
x_pos = 0
x_head = 0
y_pos = 0
block_increment = 20
game_is_on = True
game_iteration = 0
square_id = 1
snake = []

for _ in range(snake_length):
    square = Turtle("square")
    square.penup()
    #square.speed("fastest")
    square.goto(x=x_pos, y=0)
    square.color("white")
    snake.append(square)
    x_pos -= 20

screen.update()
# #old movement logic
# for i in range(10):
#     x_head = block_increment*i
#     x_pos = x_head
#     j = 1
#     print(f"round {i}")
#     for square in snake:
#         square.goto(x_pos,y=0)
#         position = square.pos()
#         print(f"{j} : {position}")
#         j +=1
#         x_pos -= 20

while game_is_on:
    print(f"--- round {game_iteration} ---")
    square_id = 1
    for square in snake:
        square.forward(block_increment)
        square_pos = square.pos()
        print(f"{square_id}: {square_pos}")
        square_id += 1
    game_iteration += 1
    time.sleep(0.5)
    screen.update()















screen.exitonclick()