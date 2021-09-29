#draw three triangles
from turtle import *

#draw first triangle
for sides in range(1,4):
    forward(40)
    left(180-60)

#move to starting poing of second triangle
penup()
right (90)
forward(100)
left(90)
pendown()

#draw second triangle
for sides in range(1,4):
    forward(40)
    left(180-60)

#move to starting poing of third triangle
penup()
forward(100)
pendown()

#draw third triangle
for sides in range(1,4):
    forward(40)
    left(180-60)
