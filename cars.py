from turtle import Turtle
import random
COLORS= ["DarkBlue","DarkCyan","DarkGoldenRod","DarkGray","DarkGreen","DarkKhaki","DarkMagenta","DarkOliveGreen","DarkOrange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkTurquoise","DarkViolet","DimGray","FireBrick","ForestGreen","Maroon","MidnightBlue","Navy","Olive","SaddleBrown"]
class Cars():

    def __init__(self):
        self.Ycor=-233
        self.obj_list = []
        for i in range(13):
            self.Ycor += 35
            t=Turtle("square")
            t.color(random.choice(COLORS))
            t.setheading(180)
            t.shapesize(stretch_wid=1,stretch_len=2)
            t.pu()
            t.goto(random.randint(200,350),self.Ycor)
            self.obj_list.append(t)
        
            for j in range(random.randint(1,1)):
                t=Turtle("square")
                t.color(random.choice(COLORS))
                t.setheading(180)
                t.shapesize(stretch_wid=1,stretch_len=2)
                t.pu()
                t.goto(random.randint(-200,250),self.Ycor)
                self.obj_list.append(t)

    def Move(self):
        for i in range(len(self.obj_list)):
            self.obj_list[i].fd(random.randint(7,20))

            for i in range(len(self.obj_list)):
                if self.obj_list[i].xcor()<-300:
                    self.obj_list[i].goto(280,random.randint(-198,235))
