import turtle as tr
import random

suzy = tr.Turtle()
tr.colormode(255)
random_dir = [0, 90, 180, 360]


def draw_color():
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = random.randint(0, 250)
    colmode = (r, g, b)
    return colmode


def draw_cir():
    for i in range(1, 37):
        suzy.pen( pencolor = draw_color(), speed= 0)
        suzy.circle(100)
        suzy.setheading(10*i)
        

draw_cir()
tr.Screen()
tr.Screen().exitonclick()