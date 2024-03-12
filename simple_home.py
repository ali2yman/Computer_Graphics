
# Run this code in turtle sandbox

import turtle
t = turtle.Turtle()
t.speed(10)

def circle(size,color):
  t.color(color)
  t.begin_fill()
  t.circle(size)
  t.end_fill()
  
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    
    t.end_fill()
  
def draw_triangle(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()
      
      
t.penup()
t.goto(-170,180)
t.pendown()

circle(30,"yellow")

t.penup()
t.goto(70,70)
t.pendown()

circle(40,(0,42,42))

t.penup()
t.goto(50,115)
t.pendown()

circle(40,(0,42,42))

t.penup()
t.goto(80,100)
t.pendown()

circle(40,"green")

t.penup()
t.goto(50,60)
t.pendown()

circle(40,(0,255,128))

t.penup()
t.goto(20,100)
t.pendown()

circle(40,(128,255,0))

t.penup()
t.goto(45,-65)
t.pendown()

draw_rectangle(20,130,(101, 67, 33))

t.penup()
t.goto(-170,-70)
t.pendown()

draw_rectangle(110,140,(0, 102, 102))

t.penup()
t.goto(-170,70)
t.pendown()

draw_triangle(110,"black")

t.penup()
t.goto(-100,10)
t.pendown()

draw_rectangle(30,30,"yellow")

t.penup()
t.goto(-160,10)
t.pendown()

draw_rectangle(30,30,"yellow")

t.penup()
t.goto(-130,-70)
t.pendown()

draw_rectangle(30,50,(51,0,102))