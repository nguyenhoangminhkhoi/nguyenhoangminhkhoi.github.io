# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020C
# Assignment: 1
# Author: Nguyen Hoang Minh Khoi (s3759804)
# Created date: 06/12/2020
# Last modified date: 13/12/2020

#Problem 1 - Histogram drawing
import turtle
import random

win = turtle.Screen()
win.bgcolor('white')
draw_axis = turtle.Turtle()
draw_axis.color('black')


#Draw axis
draw_axis.penup()
draw_axis.back(100)
draw_axis.pendown()
y_straigt = -60
val_percent = 0
for i in range(1):
    draw_axis.up()
    draw_axis.goto(170, y_straigt)
    draw_axis.down()
    draw_axis.back(350)
    draw_axis.left(90)
    draw_axis.forward(300)
#Draw percentage   
for i in range(10):
    draw_axis.up()
    y_straigt += 30
    draw_axis.goto(-180, y_straigt)
    for i in range(1):
        draw_axis.down()
        draw_axis.goto(-210, y_straigt)
        val_percent += 10
        draw_axis.write(str(val_percent), font=("Arial",12, "normal"))


#define drawing block 
def draw_blk(t, x_blk, y_blk, y_h, x_h, y):
    t.goto(x_blk,y_blk)
    draw_axis.down()
    t.forward(y_h)
    t.right(90)
    t.forward(65)
    t.goto(x_h, y_blk)
    t.left(90)
draw_axis.up()

#define drawing grade
draw_axis.up()
def draw_grade(t, x_result, y_result, w):
    t.goto(x_result, y_result)
    t.up()
    t.goto(x_result, -80)
    t.write(str(w), align="center", font=('arial',12,'normal'))

#use random function to get 100 random numbers from 1 to 100
value_one_percent = 3
number_of_hd = number_of_di = number_of_cr = number_of_pa = number_of_nn = 0
for x in range(100):
  random_number = random.randint(0, 101)
  print (random_number)
  if (random_number >= 80):
      number_of_hd += 1
  elif (random_number >= 70) :
      number_of_di += 1
  elif (random_number >= 60) :
      number_of_cr += 1
  elif (random_number >= 50) :
      number_of_pa += 1
  else :
      number_of_nn += 1
else:
  print("random finished!", number_of_hd, number_of_di, number_of_cr, number_of_pa, number_of_nn)

#Draw grade inclue percentage of each grade
draw_grade(draw_axis, -130, -60,str(number_of_hd)+'% HD')
draw_grade(draw_axis, -65, -60,str(number_of_di)+'% DI')
draw_grade(draw_axis, 0, -60,str(number_of_cr)+'% CR')
draw_grade(draw_axis, 65, -60,str(number_of_pa)+'% PA')
draw_grade(draw_axis, 130, -60,str(number_of_nn)+'% NN')

#Draw block base on percentages of each grade
draw_blk(draw_axis, -165, -60, number_of_hd * value_one_percent, -100, -60)
draw_blk(draw_axis, -100, -60, number_of_di * value_one_percent, -35, -60)
draw_blk(draw_axis, -35, -60, number_of_cr * value_one_percent, 30, -60)
draw_blk(draw_axis, 30, -60, number_of_pa * value_one_percent, 95, -60)
draw_blk(draw_axis, 95, -60, number_of_nn * value_one_percent, 160, -60)

win.exitonclick()


