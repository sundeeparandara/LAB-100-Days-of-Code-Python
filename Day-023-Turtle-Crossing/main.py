import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

cars = CarManager()


screen.listen()
screen.onkeypress(turtle.move_up, "w")
#screen.onkeypress(turtle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    turtle.reset_position()
    cars.move_cars()
    cars.check_cars_on_screen()
    #print(f"Turtle position {turtle.position()}")



screen.exitonclick()