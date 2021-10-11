#draw four squares accross the page
from turtle import *

n = 4
for square in range(1,n+1):
    #draw square
    for side in range(4):
        forward (40)
        right (90)
        
    #move to position for nexr square
    penup()
    forward (80)
    pendown()
