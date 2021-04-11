from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #distance between snake and food
    if snake.head.distance(food) < 15:
        #print("glorious food!!!")
        score.update_score()
        food.food_spawn()
        snake.extend_snake()

    #wall collision detection
    if (snake.head.pos()[0] > 280) | (snake.head.pos()[0] < -280) | (snake.head.pos()[1] > 280) | (snake.head.pos()[1] < -280):
        print("Game over. Wall Collision.")
        score.game_over()
        game_is_on = False

    #tail detection collision
    for segment in range(1,len(snake.segments)):
        if snake.head.distance(snake.segments[segment]) < 10:
            print("Game over. Snake Body Collision.")
            score.game_over()
            game_is_on = False

screen.exitonclick()