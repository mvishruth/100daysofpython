from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __int__(self):
        super.__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", move=False, align=ALINGMENT, font=FONT)
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
