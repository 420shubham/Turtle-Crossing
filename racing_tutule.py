from turtle import Turtle
import random

class Racist_Tutule(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        x_axis= random.randint(-200, 220)
        self.goto(x_axis,-233)
    

    def left(self):
        self.goto(self.xcor()-10,self.ycor())

    def right(self):
        self.goto(self.xcor()+10,self.ycor())

    def up(self):
        self.goto(self.xcor(),self.ycor()+10)
