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
x_x_a = -115
turt.up()
turt.goto(x_x_a, -60)
turt.goto(-120,-60)
turt.down()
def draw_block(t, sz):
    t.forward(sz)
    t.goto(x_x_b, 140)
    t.goto(x_x_b,-60)
x_x_b = -70 
for i in range(5):
    draw_block(turt, 200)
    x_x_b += 50
    

    
    


win.exitonclick()