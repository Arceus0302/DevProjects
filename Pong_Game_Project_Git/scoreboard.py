from turtle import Turtle
#This class sets the scoreboard and updates the scoreboard each time the user or the opponent scores.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=('Courier', 80, 'bold'))
        self.goto(100, 200)
        self.write(self.r_score, font=('Courier', 80, 'bold'))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
