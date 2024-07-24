from turtle import Screen
from cars import Cars
from racing_tutule import Racist_Tutule
from score import Score
import random
import time

s= Screen()
s.setup(width=600, height=500)
s.tracer(0)


car= Cars()
ram= Racist_Tutule()
score = Score()
s.update()

s.listen()
s.onkey(ram.left, "Left")
s.onkey(ram.right, "Right")
s.onkey(ram.up, "Up")

game_on= True
speed=0.2
while game_on:
    time.sleep(speed)
    s.update()
    car.Move()
    
    for i in range(len(car.obj_list)):
        if ram.distance(car.obj_list[i]) < 20:
            score.game_over()
            game_on=False

    if ram.ycor()>240:
        speed -=0.05
        ram.goto(random.randint(-200,220),-233)
        time.sleep(1)




s.exitonclick()