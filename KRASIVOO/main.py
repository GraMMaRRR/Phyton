import turtle as t
import colorsys
t.Screen().bgcolor("black")
k=t.Turtle()
t.tracer(10)
t.hideturtle()
h=0.3
k.pensize()
def design (ang,n):
    k.right(ang)
    k.forward(n)
    k.left(ang)
    k.back(n)
for i in range(350):
    c=colorsys.hsv_to_rgb(h,0.8,1)
    k.pencolor(c)
    design(100,i)
    k.circle(i,150)
    design(60,i)
    design(60,i)
    h+=0.006
t.done()