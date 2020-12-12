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

line_m = time.time()
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
    line_m.forward(line_m_length)
    line_h.left(90)
    line_h.forward(line_h_length)


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
    
    if line_s == 60:
        line_s = 0
        line_m.clear()
        line_m.up()
        line_m.home()
        line_m.down()
        x = line_m_length * math.sin(math.radians(angle_1))
        y = line_m_length * math.cos(math.radians(angle_1))
        line_m.goto(x, y)
        angle_1 += 6
    
    if line_m == 15:
        line_h == 0.25
        line_h.clear()
        line_h.up()
        line_h.home()
        line_h.down()
        x = line_h_length * math.sin(math.radians(angle_1))
        y = line_h_length * math.cos(math.radians(angle_1))
        line_h.goto(x, y)
        angle_1 += 7.5
    
    window.update()

window.exitonclick()
