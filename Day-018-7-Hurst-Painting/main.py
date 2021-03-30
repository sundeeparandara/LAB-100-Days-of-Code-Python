import colorgram
import random
from turtle import Turtle, Screen

rows = 5
columns = 5
space_between_dots = 100
dot_radius = 20

#create a painter
painter = Turtle()
painter.speed("fastest")

#extract colors
colors = colorgram.extract('image.png',10)
rgb_list = []
color = colors[0]
for color in colors:
    r = color.rgb.r / 255
    g = color.rgb.g / 255
    b = color.rgb.b / 255
    rgb_list.append((r,g,b))

#generate coordinates

cood_list = []
cood_y = 0
cood_x = 0
for r in range(rows):
    cood_y = space_between_dots*r
    for c in range(columns):
        cood_x = space_between_dots*c
        cood_list.append((cood_x,cood_y))

#random color dot drawing function
def draw_dots(radius,color_tuple):
    painter.pendown()
    painter.color(color_tuple)
    painter.begin_fill()
    painter.circle(radius)
    painter.end_fill()
    painter.penup()

#draw a hurst
for cood in cood_list:
    painter.setpos(cood)
    draw_dots(dot_radius,random.choice(rgb_list))


screen = Screen()
screen.exitonclick()