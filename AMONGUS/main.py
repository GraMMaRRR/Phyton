from turtle import *



fillcolor('green')
begin_fill()
pensize(10)
right(90)
forward(50)
for n in [
    (30,200), (90,200), (30,50)
]:
    circle(n[0], 180)
    forward(n[1])
right(90)
forward(60)
end_fill()


penup()
goto(0, 100)
pendown()
fillcolor('white')
begin_fill()
for i in range(2):
    forward(50)
    circle(40, 180)
end_fill()