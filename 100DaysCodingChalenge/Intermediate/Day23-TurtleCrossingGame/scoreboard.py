from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-220,260)
        self.write(f"Level {self.level}",align="center",font=FONT)

    def game_over(self):
        #self.clear()
        self.goto(0, 260)
        self.write(f"GAME OVER...", align="center", font=FONT)




