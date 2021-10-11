#draw 4 squares growing in size
from turtle import *

shapes = 4

for shape in range(1, shapes+1):
    #draw square
    for sides in range(4):
        forward(40+10*(shape-1))
        left(90)
    #move in position for next square
    penup()
    forward(10+40+10*(shape-1))
    pendown()            


##declare the number of squares you want
##for each square:
##    >> draw square
##       for sides from 1 to 4
##           move forward by 40 + ((square no - 1)*10)
##           rotate by 90 degrees
##    >> move in position for next square
##        lift pen
##        move 80 units
##        put pen down
##
##square 1: 40 = sides 1 + 0 ((square no - 1)*10)
##square 2: 50 = sides1 + 10 ((square no - 1)*10)
##square 3: 60 = sides1 + 20 ((square no - 1)*10)

