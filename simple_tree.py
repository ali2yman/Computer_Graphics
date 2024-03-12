import turtle
t = turtle.Turtle()
t.speed(10)

t.color("green")
t.penup()
t.goto(0,100)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()



t.color("yellow")
t.penup()
t.goto(50,50)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()


t.color("green")
t.penup()
t.goto(0,0)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()


t.color("yellow")
t.penup()
t.goto(-50,50)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()


t.color("green")
t.penup()
t.goto(-50, -70)
t.pendown()
t.forward(100)
t.backward(50)
t.left(90)
t.forward(100)



