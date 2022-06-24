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

for i in range(100):
    suzy.pen(pensize= 15, pencolor=draw_color(), speed=10)
    suzy.fd(30)
    suzy.setheading(random.choice(random_dir))




tr.Screen()
tr.Screen().exitonclick()