from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto (-220, 250)
        self.write(f"Level: {self.level}", True, align="center", font=('Courier', 18, 'bold'))

    def next_level(self):
        self.level += 1
        self.clear()
        self.penup()
        self.goto (-220, 250)
        self.write (f"Level: {self.level}", True, align="center", font=('Courier', 18, 'bold'))

    def game_over(self):
        self.clear ()
        self.penup ()
        self.goto (0, 0)
        self.write (f"🐢 GAME OVER Unu 🐢", True, align="center", font=('Courier', 18, 'bold'))
