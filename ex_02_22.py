#draw an upper right right-angled triangle

size = 5

for line in range(1, size+1):
    for space in range (line - 1):
        print(' ',end = '')
    for asterisk in range (size - line + 1):
        print('*',end = '')
    print()

##***
## **
##  *
##  
##for each line in the triangle:
##    draw space for the number for (line - 1)
##        line 1: 0 space
##        line 2: 1 space
##        line 3: 2 space 
##    draw the number of asterisk of (size - line + 1)
##        3 asterisk for line 1
##        2 asterisks for line 2
##        1 asterisk for line 3
