from turtle import *

t = Turtle()

def draw_rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    
    t.end_fill()

# Draw the outer rectangle
draw_rectangle(300, 150, 'blue')

# Calculate the position to center the inner rectangle
inner_width = 260
inner_height = 110
center_x = (300 - inner_width) / 2
center_y = (150 - inner_height) / 2

# Move to the calculated position
t.penup()
t.goto(center_x, center_y)
t.pendown()

# Draw the inner rectangle
draw_rectangle(inner_width, inner_height, 'red')

done()
