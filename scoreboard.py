from turtle import  *
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)

    def score(self):
        self.clear()
        self.write(f"Level : {self.level} ", align="left", font=FONT)

    def in_score(self):
        self.level += 1
        self.score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="centre",font=FONT)