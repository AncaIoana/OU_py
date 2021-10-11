#draw the quarterly sales graph
from turtle import *

#setup variables for gloves sales, where 1 unit represents 1 million gloves sold
gloves1 = 10
gloves2 = 8
gloves3 = 3
gloves4 = 5

#draw x-axis
goto(80,0)

#draw y-axis
goto(0,0)
goto(0,100)

#plot data, where 10 units represents 1 million gloves sold
goto(0,0)
goto(20, gloves1 * 10)
goto(40, gloves2 * 10)
goto(60, gloves3 * 10)
goto(80, gloves4 * 10)
