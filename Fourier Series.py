import turtle
from math import *
wn= turtle.Screen()
wn.title("Fourier Series")
t = turtle.Turtle()
p = turtle.Turtle()
wn.tracer(0)
p.hideturtle()
p.goto(-200,0)
p.fd(400)
p.stamp()
p.home()
p.goto(0,150)
p.left(90)
p.stamp()
p.goto(0,-150)
wn.tracer(1)
wn.update()
t.pu()
t.goto(-200,0)
t.pd()

for x in range(-200,201,1):
    sigma = 0
    for n in range(1,29):
        sigma+=(200/(n*pi))*sin(n*pi/2)*cos((n*pi*x)/200)
    y = 50 + sigma
    t.goto(x,y)

turtle.done()