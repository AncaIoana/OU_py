#draw the quarterly sales graph
from turtle import *

#setup variables for gloves sales, where 1 unit represents 1 million gloves sold
gloves = [10,8,3,5]

#draw x-axis
goto(80,0)

#draw y-axis
goto(0,0)
goto(0,100)

#plot data, where 10 units represents 1 million gloves sold
goto(0,0)
j = 0
for i in range(len(gloves)):
    j = j + 20
    goto(j,gloves[i]*10)

