import turtle

t = turtle.Turtle()
t.speed(2)

t.color("#F65314")
t.begin_fill()
t.penup()
t.goto(-250,200)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.color("#7CBB00")
t.begin_fill()
t.penup()
t.goto(-140, 200)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.color("#FFBB00")
t.begin_fill()
t.penup()
t.goto(-140, 90)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.color("#00A1F1")
t.begin_fill()
t.penup()
t.goto(-250, 90)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.pencolor("black")
t.penup()
t.goto(-20, 50)
t.pendown()
t.pensize(12)
t.write('Microsft',font=('calibri',50,'bold'))
t.hideturtle()
turtle.done()

     
