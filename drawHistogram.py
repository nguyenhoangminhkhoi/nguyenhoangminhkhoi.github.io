import turtle

win = turtle.Screen()
win.bgcolor('white')
turt = turtle.Turtle()
turt.color('black')

turt.penup()
turt.back(100)
turt.pendown()

x_y = -180
y_y = -60

val_y = 0

for i in range(1):
    turt.up()
    turt.goto(170, y_y)
    turt.down()
    turt.back(350)
    turt.left(90)
    turt.forward(300)
    
for i in range(10):
    turt.up()
    y_y += 30
    turt.goto(x_y, y_y)
    for i in range(1):
        turt.down()
        turt.goto(-210, y_y)
        val_y += 10
        turt.write(str(val_y), font=("Arial",12, "normal"))
turt.up()
def draw_grade(t, x_g, y_g, w):
    t.goto(x_g, y_g)
    t.up()
    t.goto(x_g, -80)
    t.write(str(w), align="center", font=('arial',12,'normal'))
draw_grade(turt, -130, -60,'HD')
draw_grade(turt, -65, -60,'DI')
draw_grade(turt, 0, -60,'CR')
draw_grade(turt, 65, -60,'PA')
draw_grade(turt, 130, -60,'NN')
def draw_blk(t, x_b, y_b, y_h, x_h, y):
    t.goto(x_b,y_b)
    turt.down()
    t.forward(y_h)
    t.right(90)
    t.forward(65)
    t.goto(x_h, y_b)
    t.left(90) 
turt.up()
draw_blk(turt, -165, -60, 60, -100, -60)
draw_blk(turt, -100, -60, 150, -35, -60)
draw_blk(turt, -35, -60, 45, 30, -60)
draw_blk(turt, 30, -60, 35, 95, -60)
draw_blk(turt, 95, -60, 10, 160, -60)


    
    


win.exitonclick()