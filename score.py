from turtle import Turtle
import time

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("bisque4")
        self.speed(0)

    def create(self):
        self.goto(0, 0)
        self.pd()

    def game_over(self):
        self.create()
        self.write("Game Over! You are racist", align="center", font=("Courier", 24, "bold"))
    

        