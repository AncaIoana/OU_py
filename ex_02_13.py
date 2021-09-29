#Draw a house
from turtle import *

#Draw front wall
for sides in range(1,5):
    forward(100)
    right(90)

#Draw the door
right(90)
forward(100)
left(90)
forward(10)
left(90)
forward(75)
right(90)
forward(30)
right(90)
forward(75)

#Position for window
penup()
left(90)
forward(20)
left(90)
forward(75)
right(90)
pendown()

#Draw window
for sides in range(1,5):
    forward(30)
    right(90)

#Position the roof
penup()
left(90)
forward(25)
right(90)
forward(50)
left(180)
pendown()

#Draw the roof
for sides in range(1,4):
    forward(120)
    right(180-60)

    
