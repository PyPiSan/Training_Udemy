import turtle as tr
import random

suzy = tr.Turtle()
suzy.penup()
suzy.setposition(-50, 150)
suzy.pendown()
tr.colormode(255)

def draw_color():
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = random.randint(0, 250)
    colmode = (r, g, b)
    return colmode

def draw_shapes(ang):
    suzy.fd(100)
    suzy.rt(ang)

i = 3
while i<= 10:
    j = 1
    # rang = draw_color()
    suzy.pencolor(draw_color())
    while j <=i:
        draw_shapes(360/i)
        j+=1
    i+=1




tr.Screen()
tr.Screen().exitonclick()