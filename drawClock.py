import turtle
import random
import math
import time

window = turtle.Screen()
window.bgcolor("white")
window.tracer(0)
window.screensize(400)

line_s = turtle.Turtle()
line_s.color("red")
line_s.pensize(3)
line_s.hideturtle()

line_m = turtle.Turtle()
line_m.color("black")
line_m.pensize(5)
line_m.hideturtle()

line_h = turtle.Turtle()
line_h.color("black")
line_h.pensize(5)
line_h.hideturtle()

turt = turtle.Turtle()
turt.color("black")
turt.pensize(5) 
turt.speed(10)

line_s_length = 200
line_m_length = 170
line_h_length = 150

seconds = 60
hours = 12
radius = 200
angle_1 = 360 / seconds
val = 13
angle_m = 6
angle_h = 6
for i in range(hours): 
    val -= 1     
    turt.up()
    turt.left(90)             
    turt.forward(radius)
    turt.down()
    turt.forward(10) 
    turt.write(str(val), align="center",font=("Arial",12, "normal"))       
    turt.up()          
    turt.goto(0, 0)         
    turt.right(60)
        
for i in range (1):
    line_s.left(90)
    line_s.forward(line_s_length)
    line_m.left(90)
    line_m.forward(line_m_length)
    line_h.left(90)
    line_h.forward(line_h_length)

s_counter = 0
m_counter = 0
h_counter = 0
while True:
    s_counter+=1
    
    line_s.clear()
    line_s.up()
    line_s.home()
    line_s.down()
    x = line_s_length * math.sin(math.radians(angle_1))
    y = line_s_length * math.cos(math.radians(angle_1))
    line_s.goto(x, y)
    angle_1 += 6
    

    time.sleep(0.001)
    
    if s_counter % 60 == 0:
       
        print(m_counter)
        line_m.clear()
        line_m.up()
        line_m.home()
        line_m.down()
        x = line_m_length * math.sin(math.radians(angle_m))
        y = line_m_length * math.cos(math.radians(angle_m))
        line_m.goto(x, y)
        angle_m += 6
       
    if s_counter % 720 == 0:
        line_h.clear()
        line_h.up()
        line_h.home()
        line_h.down()
        x = line_h_length * math.sin(math.radians(angle_h))
        y = line_h_length * math.cos(math.radians(angle_h))
        line_h.goto(x, y)
        angle_h += 6
    
    window.update()

window.exitonclick()
