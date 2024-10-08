from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 20, 'bold')
#The class which shows and update the scoreboard of the game.
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.text") as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score : {self.score} High score {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.text", "w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()



