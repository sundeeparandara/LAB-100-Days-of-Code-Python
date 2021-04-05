import colorgram
import random
from turtle import Turtle, Screen

#params
rows = 5
columns = 5
space_between_dots = 100
dot_radius = 20

#create a painter
painter = Turtle()
painter.speed("fastest")
painter.penup()
start_x = int((-1 * columns * space_between_dots)/2)
start_y = int((-1 * rows * space_between_dots)/2)
screen_x = (columns) * space_between_dots
screen_y = (rows) * space_between_dots
screen_pad = 50

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
cood_x = 0
offset_x = start_x + screen_pad
cood_y = 0
offset_y = start_y + screen_pad
for r in range(rows):
    cood_y = space_between_dots*r + offset_y
    for c in range(columns):
        cood_x = space_between_dots*c + offset_x
        cood_list.append((cood_x,cood_y))

print(cood_list)

#random color dot drawing function
def draw_dots(radius,color_tuple):
    painter.pendown()
    painter.color(color_tuple)
    painter.begin_fill()
    painter.circle(radius)
    painter.end_fill()
    painter.penup()

#generate screen
screen = Screen()
screen.bgcolor(0,0,0)
screen.setup(width=screen_x,height=screen_y)


#draw a hurst
for cood in cood_list:
    painter.setpos(cood)
    draw_dots(dot_radius,random.choice(rgb_list))


screen.exitonclick()