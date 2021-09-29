# Draw two squares
from turtle import *

#draw square
for sides in range(1,5):
    forward(40)
    right(90)

#move to start of next square
penup()
right(90)
forward(60)
left(90)
pendown()

#draw square
for sides in range(1,5):
    forward(40)
    right(90)
