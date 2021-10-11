#draw a lower right right-angled triangle from asterisks
size = 3

for line in range(1, size+1):
    for space in range(size - line+1):
        print(' ',end = '')
    for asterisk in range(line):
        print('*', end='')
    print()
