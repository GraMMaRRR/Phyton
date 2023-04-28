import time
from turtle import *
bgcolor('black')
hideturtle()
penup()
for p in [1,2,3]:
    goto(p * 30, 30)
    dot(15, 'brown')
while True:
    for n in [0, 30]:
        k = Turtle()
        k.goto(0, 50)
        k.color('yellow')
        k.speed(11)
        k.hideturtle()
        k.left(150)
        k.begin_fill()
        k.circle(50, 270 + n)
        k.left(90)
        k.forward(50)
        k.end_fill()
        time.sleep(0.1)
        if n == 30:
            k.clear()
done()