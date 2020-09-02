import turtle
import random
t=turtle.Turtle()
t.shape("turtle")

for turn in range(30):
    length = random.randint(1,100)
    t.forward(length)
    angle = random.choice[90,180,270,360]
    t.left(angle)
