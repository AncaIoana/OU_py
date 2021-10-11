#print 4 triangles of growing sizes

from turtle import *

shapes = 4

for triangle in range(1, shapes+1):
    #draw triangle
    for sides in range(3):
        forward(40 + 10 * (triangle - 1))
        left(180-60)
    #move in position for next triangle
    penup()
    forward(10 + 40 + 10 * (triangle-1))
    pendown()

##declare the number of triangles
##for each triangle
##    >>draw triangle
##    for each side from 1 to 3
##        move forward 40
##        turn left (180-60)
##    >>move in position for next triangle
##        lift pen
##        move forward side + 10
##        put pen down
##
##triangle 1: side = 40
##triangle 2: side = 50 = 40 + (10*(triangle number - 1))
##triangle 3: side = 60 = 40 + (10*(triangle number - 1))
