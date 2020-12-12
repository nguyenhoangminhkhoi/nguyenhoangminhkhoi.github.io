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

line_s = turtle.Turtle()
line_m = turtle.Turtle()
line_h = turtle.Turtle()
turt = turtle.Turtle()

line(line_s, 'red', 5, 10)
line(line_m, 'black', 5, 10)
line(line_h, 'grey', 5, 10)
line(turt, 'black', 5, 10)
def draw_line(t, sz):
    for i in range(1):
        t.left(90)
        t.forward(sz)
sz = 200            
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
sz = 250        
draw_clk(turt, sz, 60, 6)  
seconds = 60
hours = 12
radius = 200
angle_1 = 360 / seconds
val = 13
for i in range(hours):
    val -= 1
    turt.up()
    turt.left(90)             
    turt.forward(230)
    turt.down()
    turt.forward(30)
    turt.up()
    turt.forward(20) 
    turt.write(str(val), align="center", font=("Arial",12, "normal"))       
    turt.up()          
    turt.goto(0, 0)         
    turt.right(60)

while True:
    line_s.clear()
    line_s.up()
    line_s.home()
    line_s.down()
    x = sz * math.sin(math.radians(angle_1))
    y = sz * math.cos(math.radians(angle_1))
    line_s.goto(x, y)
    angle_1 += 6

    time.sleep(0.5)
win.exitonclick()