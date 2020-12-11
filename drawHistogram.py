import turtle

def draw_line(t, lg, w):
    t.pensize(w)
    for i in range(1):
        t.forward(lg)
        t.left(90)
        t.forward(20)

win = turtle.Screen()
win.bgcolor('white')
turt = turtle.Turtle()
turt.color('black')

turt.penup()
turt.back(100)
turt.pendown()

val = 10 

for i in range(10):
    val += 10
    draw_line(turt, 100, 5)
    turt.write(str(val), align="center",font=("Times new roman",12, "normal"))
    turt.penup()
    turt.back(100)
    turt.pendown()
   
    
    


win.exitonclick()