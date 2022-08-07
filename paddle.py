from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.paddle = Turtle()
        self.position = position
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6, outline=None)
        self.setheading(90)
        self.setpos(self.position)

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(30)

