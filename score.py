from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=270)
        self.update_score()


    def update_score(self):
        self.write(arg=f"Score: {self.score} ", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=" Game Over", align="center", font=("Courier", 30, "normal"))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
