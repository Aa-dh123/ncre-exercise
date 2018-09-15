from turtle import *
from random import *

def drawsnow():
    hideturtle()
    pensize(2)

    for i in range(50):
        r,g,b = random(),random(),random()
        color(r,g,b)
        penup()
        setx(randint(-370,380))
        sety(randint(1,270))
        pd()
        dens = randint(8,12)
        snowsize = randint(7,12)
        for j in range(dens):
            forward(snowsize)
            backward(snowsize)
            right(360/dens)

def drawground():
    hideturtle()

    for i in range(500):
        pensize(randint(8,13))
        x = randint(-400,350)
        y = randint(-280,-1)
        r,g,b = -y/280,-y/280,-y/280
        pencolor = ((r,g,b))
        penup()
        goto(x,y)
        pd()
        forward(randint(40,100))

setup(800,600,200,200)
tracer(False)
bgcolor('black')
drawsnow()
drawground()
done()


        
        
        
