from turtle import *

t = Turtle()

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    
    t.end_fill()

# Function to draw a circle
def draw_circle(radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()



# Draw the robot body
draw_rectangle(225, 200, "blue")

t.penup()
t.goto(107.5,200)
t.pendown()

# Draw the robot head
draw_circle(50, "red")

t.penup()
t.goto(225,170)
t.pendown()

# draw the hand 
draw_rectangle(150,30,"yellow")

t.penup()
t.goto(-150,170)
t.pendown()

draw_rectangle(150,30,"yellow")

t.penup()
t.goto(165,-150)
t.pendown()
# draw the leg 
draw_rectangle(30,150,"green")

t.penup()
t.goto(35,-150)
t.pendown()

draw_rectangle(30,150,"green")


# Keep the window open
done()
