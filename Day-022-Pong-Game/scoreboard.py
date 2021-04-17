from turtle import Turtle

FONT_STYLE = ("Courier",80,"normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align=ALIGNMENT,font=FONT_STYLE)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT_STYLE)

    def update_score_left(self):
        self.l_score += 1
        self.write_score()

    def update_score_right(self):
        self.r_score += 1
        self.write_score()
