from turtle import *

t = Turtle()  
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)  
    t.end_fill()

draw_circle(75, 'red')

t.penup()
t.goto(150, 0)
t.pendown()

draw_circle(75, 'blue')

done()  
