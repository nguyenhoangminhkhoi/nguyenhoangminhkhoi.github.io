# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Hoang Minh Khoi (s3759804)
# Created date: 06/12/2020
# Last modified date: 13/12/2020

#Problem 2 - Clock drawing and New Year count down
import turtle
import turtle
import random
import math
import time
from datetime import datetime

now = datetime.now()

#Preparation for hands and clock
win = turtle.Screen()
win.screensize(500)
win.tracer(0)

line_s = turtle.Turtle()
line_m = turtle.Turtle()
line_h = turtle.Turtle()
clock_frame = turtle.Turtle()
digital_clock = turtle.Turtle()
block_str = turtle.Turtle()
countdown_turtle = turtle.Turtle()
# define hands and turtle
def line(t, color, pensize):
    t.color(color)
    t.pensize(pensize)
    t.hideturtle()
line(line_s, 'red', 5)
line(line_m, 'black', 5)
line(line_h, 'black', 5)
line(clock_frame, 'black', 5)
line(digital_clock,'black', 5)
line(block_str,'black', 5)
line(countdown_turtle,'black', 5)
#The counter will be the same with the current time
s_counter = now.second
m_counter = now.minute
h_counter = now.hour
today = str(now.strftime("%Y/%m/%d"))
d_counter = int(now.strftime("%d"))
s_2counter  = now.second
m_2counter  = now.minute 
h_2counter  = now.hour
new_year = datetime(now.year + 1, 1, 1)

# Change formula here so we can have the correct angle and length for each line
angle_s =  360 / 60 * s_counter
angle_m =  360 / 60 * m_counter
angle_h =  360 / 12 * h_counter 

line_s_length = 150
line_m_length = 140
line_h_length = 120

#draw clock without numbers 
seconds = 60
def draw_clk(t, sz, sec, agl):
    for i in range(sec):
        t.up()
        t.forward(sz)
        t.down()
        t.forward(5)
        t.up()
        t.goto(0, 0)
        t.right(agl)       
draw_clk(clock_frame, 170, seconds, 6) 

# draw numbers from 1 to 12 on the clock
val = 12 
radius = 150
hours = 12
for i in range(hours):  
    clock_frame.hideturtle()
    clock_frame.up()
    clock_frame.left(90)             
    clock_frame.forward(radius)
    clock_frame.down()
    clock_frame.forward(20)
    clock_frame.up()
    clock_frame.forward(20) 
    clock_frame.write(str(val), align="center",font=("arial",12, "normal"))       
    clock_frame.up()          
    clock_frame.goto(0, 0)         
    clock_frame.right(60)
    val -= 1 


#draw block
# Use new turtle to demonstrate the countdown 
block_str.up()
block_str.goto(-200, -210)
block_str.down()
for i in range(2):
    block_str.forward(400)
    block_str.right(90)
    block_str.forward(50)
    block_str.right(90)
block_str.up()
block_str.goto(-100, -230)    
block_str.write(str("Current time is ") + str(today) , align="center", font=("arial", 12, "normal"))
block_str.goto(-50, -250)

digital_clock.goto(50, -230)
digital_clock.hideturtle()
countdown_turtle.goto(-170, -250)
# set up lines
def set_up_line(t, sz, agl):
    t.clear()
    t.up()
    t.home()
    t.down()
    x = sz * math.sin(math.radians(agl))
    y = sz * math.cos(math.radians(agl))
    t.goto(x, y)
    agl += 6
set_up_line(line_s, line_s_length, angle_s)
set_up_line(line_m, line_m_length, angle_m)
set_up_line(line_h, line_h_length, angle_h)

#make the clock runs
while True:
    #second 
    s_counter += 1
    line_s.clear()
    line_s.up()
    line_s.home()
    line_s.down()
    x = line_s_length * math.sin(math.radians(angle_s))
    y = line_s_length * math.cos(math.radians(angle_s))
    line_s.goto(x, y)
    angle_s += 6

    time.sleep(1)

    digital_clock.clear()
    countdown_turtle.clear()
    # Set up for countdown
    now = datetime.now()
    countdown = new_year - now
    days_left = countdown.days
    hours_left = (countdown.days * 24 - now.hour - 1) % 24
    minute_left = (countdown.days * 24 * 60 - now.minute - 1) % 60
    second_left = (countdown.days * 24 * 60 * 60 - now.second - 1) % 60
    # Write countdown
    countdown_turtle.write( "There are " + str(days_left) + " day " + str(hours_left) + " hours " + str(minute_left) + " minutes " + str(second_left).zfill(2) + " seconds left", 
        font =("Arial", 12, "normal")) 

    digital_clock.write(str(h_2counter).zfill(2)
            +":"+str(m_2counter).zfill(2)+":"
            +str(s_2counter).zfill(2),
            font =("Arial", 12, "normal")) 
    s_2counter += 1
    if s_2counter == 60:
        s_2counter = 0
        m_2counter += 1
   
    if s_counter % 60 == 0: 
        line_m.clear()
        line_m.up()
        line_m.home()
        line_m.down()
        x = line_m_length * math.sin(math.radians(angle_m))
        y = line_m_length * math.cos(math.radians(angle_m))
        line_m.goto(x, y)
        angle_m += 6
        m_counter += 1
    #hour
    if m_2counter == 60:
        m_2counter = 0 
        h_2counter += 1
    if s_counter % 720 == 0:
        line_h.clear()
        line_h.up()
        line_h.home()
        line_h.down()
        x = line_h_length * math.sin(math.radians(angle_h))
        y = line_h_length * math.cos(math.radians(angle_h))
        line_h.goto(x, y)
        angle_h += 6

    
    win.update()
        
win.exitonclick()

