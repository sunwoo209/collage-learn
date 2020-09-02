import turtle
import random

t = turtle.Turtle()
t.shape("turtle")



for i in range(30):
    length = random.randint(1,100)
    t.forward(length)
    qstw=random.choice([90,180,270,360])
    angle = qstw
    t.right(angle)
