from turtle import Screen, Turtle
from turtle_maker import TurtleMaker
import random

screen_width = 500
screen_height = 400
screen_border_pad = 20
colors = ["red","orange","yellow","green","blue","purple"]
start_x = int(screen_border_pad + screen_width/-2)
start_y = int(screen_border_pad + screen_height/-2)
turtle_vertical_spacing = (screen_height - 2*screen_border_pad)/(len(colors)-1)


screen = Screen()
screen.setup(width=screen_width, height=screen_height)
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
user_bet = user_bet.lower()

turtle_squad = []
for color in colors:
    turtle_squad.append(TurtleMaker(color,start_x,start_y))
    start_y += turtle_vertical_spacing

scribbler = Turtle()
scribbler.hideturtle()
style = ('Courier', 30)

within_bounds = True
while within_bounds:
    the_one = random.choice(turtle_squad)
    the_one.move_forward(10)
    if the_one.check_position()[0] >= (screen_width/2):
        within_bounds = False
        the_winner = the_one.get_color()
        if user_bet == the_winner:
            print("You won the bet.")
            scribbler.write("You won the bet.", font=style, align='center')
        else:
            print("You lost the bet.")
            scribbler.write("You lost the bet.", font=style, align='center')


screen.exitonclick()

