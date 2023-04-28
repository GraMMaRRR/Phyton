from turtle import *

hideturtle()
x = ('Calibri', 30, 'bold')
write('amazon', font=x)

up()
goto(20, 5)
down()
color('orange')
right(35)

for x,y in zip(
    [3,4,5,4,3],
    [10,10,30,10,10]
):
    width(x)
    circle(50, y)

up()
goto(73, 9)
down()
right(32)
forward(8)
right(100)
forward(8)