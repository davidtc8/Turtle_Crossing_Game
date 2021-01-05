from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        x_stays_the_same = self.xcor ()
        new_y = self.ycor () + MOVE_DISTANCE
        self.goto (x_stays_the_same, new_y)
