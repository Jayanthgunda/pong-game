from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        # self.setposition(280, 0)
        # self.setpos(0, 230)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.create_board()

    def create_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="left", font=("Courier", 40, "normal"))
        # self.write("-------", align="left", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="right", font=("Courier", 40, "normal"))

    def increase_left(self):
        self.l_score += 1
        self.create_board()

    def increase_right(self):
        self.r_score += 1
        self.create_board()
