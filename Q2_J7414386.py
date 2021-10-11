#draw a set of triangles balancing on each other

from turtle import *

no_of_triangles = 4

for triangle in range(1, no_of_triangles + 1):
    #draw triangle
    for sides in range(3):
        forward(20 + 20*(triangle-1))
        left(180-60)
    #go to position for the next triangle
        
    penup()
    left(60)
    forward(20 + 20 * (triangle-1))
    left(180-60)
    forward((20 + 20 * triangle)/2)
    right(180)
    pendown()
