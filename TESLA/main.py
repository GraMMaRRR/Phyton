import turtle

tur = turtle.Turtle()

tur.getscreen().bgcolor("red")
tur.pencolor("black")

tur.speed(10)

tur.color("white")
tur.penup()
tur.goto(-160,160)
tur.pendown()

tur.begin_fill()
tur.left(18)
tur.circle(-500,40)
tur.right(90)
tur.forward(17)

tur.right(89.5)
tur.circle(500,39)
tur.right(90)
tur.forward(17)
tur.end_fill()


tur.penup()
tur.goto(-155,133)
tur.pendown()

tur.begin_fill()
tur.right(90.5)
tur.circle(-500,38)
tur.right(70)
tur.circle(-30,80)
tur.left(90)
tur.circle(-20,-70)
tur.right(10)
tur.circle(-300,-15)
tur.right(93)
tur.forward(280)
tur.right(160)
tur.forward(280)
tur.left(80)
tur.circle(300,15)
tur.circle(20,70)
tur.left(80)
tur.circle(30,-80)
tur.end_fill()

tur.penup()
tur.goto(-20,155)
tur.pendown()
tur.pencolor("black")
tur.color("red")
tur.begin_fill()
tur.left(30)
tur.forward(60)
tur.left(130)
tur.forward(65)
tur.end_fill()

turtle.done()