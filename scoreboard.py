from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.paddle1_score = 0
        self.paddle2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.paddle2_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.paddle1_score, align='center', font=('Courier', 80, 'normal'))

    def paddle1_point(self):
        self.paddle1_score += 1
        self.update_scoreboard()

    def paddle2_point(self):
        self.paddle2_score += 1
        self.update_scoreboard()