from turtle import *
t=Turtle()
t.speed(0)

t.penup()
t.goto(0,-100)
t.pendown()

t.fillcolor("blue")
t.begin_fill()

for _ in range(4):
  t.circle(50,90)
  t.fd(100)
t.end_fill()


t.penup()
t.goto(-50,-70)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
t.circle(70)
t.end_fill()

t.penup()
t.goto(-20,10)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(12)
t.end_fill()

t.penup()
t.goto(-80,10)
t.pendown()

t.fillcolor("black")
t.begin_fill()
t.circle(12)
t.end_fill()

t.penup()
t.goto(-90,-20)
t.pendown()
t.lt(-75)

t.fillcolor("red")
t.begin_fill()
t.circle(40,150)
t.end_fill()




t.hideturtle()