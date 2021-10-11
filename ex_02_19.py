#draw four triangles accoess the page
from turtle import *

shapes = 4

for triangle in range(1, shapes+1):
    #draw a triangle
    for sides in range(1, 4):
        forward(60)
        left(180-60)
             
    #move to position for next triangle
    penup()
    forward(75)
    pendown()
