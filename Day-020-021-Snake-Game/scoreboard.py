from turtle import Turtle

ALIGNMENT = "center"
FONT_PARAM = ("Arial",20,"bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.message = "Score : 0"
        self.color("white")
        self.penup()
        self.hideturtle()

        self.score_cood_x = 0
        self.score_cood_y = 260
        self.goto(self.score_cood_x, self.score_cood_y)

        self.write_scoreboard()

    def update_score(self):
        self.score += 1
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.message = f"Score : {self.score}"
        self.write(self.message, align=ALIGNMENT,font=FONT_PARAM)

    def game_over(self):
        self.score_cood_x = 0
        self.score_cood_y = 0
        self.goto(self.score_cood_x, self.score_cood_y)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_PARAM)