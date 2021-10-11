#reverse the order of the list

#create list
gloves = [10,8,3,5]

#replace first and last elements
temp = gloves[0]
gloves[0] = gloves[3]
gloves[3] = temp

#replace second and third elements
temp = gloves[1]
gloves[1] = gloves[2]
gloves[2] = temp

print(gloves)
