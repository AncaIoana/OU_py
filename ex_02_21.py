#draw an upper left right-angled triangle

size = 3

for line in range(1, size+1):
    for asterisk in range(size - line + 1):
        print('*',end = '')
    print()    


#declare the size - how big the triangle
    #for each line draw the same number of asterisks as size - line + 1
    #move to next line

        #example:
        #line 1: draw (3 - 1 + 1) asterisks
        #line 2: draw (3 - 2 + 1) asterisks
        #line 3: draw (3 - 3 + 1) asterisks
