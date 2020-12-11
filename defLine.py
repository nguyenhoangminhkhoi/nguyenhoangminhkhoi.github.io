import turtle
import random
import math
import time

def line(t, color, pensize, speed):
    t.color(color)
    t.pensize(pensize)
    t.speed(speed)

win = turtle.Screen()
win.screensize(400)
win.tracer(0)

line_s = turtle.Turtle()
line_m = turtle.Turtle()
line_h = turtle.Turtle()
turt = turtle.Turtle()

line(line_s, 'red', 5, 5)
line(line_m, 'black', 5, 5)
line(line_h, 'grey', 5, 5)
line(turt, 'black', 5, 5)
def draw_line(t, sz):
    for i in range(1):
        t.left(90)
        t.forward(sz)
        
draw_line(line_s, 200)
draw_line(line_m, 190)
draw_line(line_h, 170)

def draw_clk(t, sz, sec, agl):
    for i in range(sec):
        t.up()
        t.forward(sz)
        t.down()
        t.forward(10)
        t.up()
        t.goto(0, 0)
        t.right(agl)

draw_clk(turt, 210, 60, 6)  
line_s_length = 200
angle_1 = 30
while True:
    line_s.clear()
    line_s.up()
    line_s.home()
    line_s.down()
    x = line_s_length * math.sin(math.radians(angle_1))
    y = line_s_length * math.cos(math.radians(angle_1))
    line_s.goto(x, y)
    angle_1 += 6

    time.sleep(0.05) 




win.exitonclick()