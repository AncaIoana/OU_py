#Draw a stick person
from turtle import *

#Draw the head
for sides in range(1,5):
    forward(40)
    right(90)

#Position for torso
penup()
right(90)
forward(40)
left(90)
forward(20)
pendown()
    
#Draw torso
right(90)
forward(80)

#position for left arm
penup()
right(180)
forward(60)
pendown()

#Draw left arm
left(180-45)
forward(30)

#Position for right arm
penup()
left(180)
forward(30)
right(90)
pendown()

#Draw right arm
forward(30)

#Position for left leg
penup()
left(180)
forward(30)
left(180-45)
forward(60)
pendown()

#Draw left leg
right(45)
forward(40)

#Position for right leg
penup()
left(180)
forward(40)
right(90)
pendown()

#Draw right leg
forward(40)
