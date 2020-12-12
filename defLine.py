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
win.tracer(10)

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
sz = 250        
draw_clk(turt, sz, 60, 6)  
val = 13
for i in range(12):
    val -= 1
    turt.up()
    turt.left(90)             
    turt.forward(sz)
    turt.down()
    turt.forward(30)
    turt.up()
    turt.forward(20) 
    turt.write(str(val), align="center", font=("Arial",12, "normal"))       
    turt.up()          
    turt.goto(0, 0)         
    turt.right(60)

win.exitonclick()