str=""
j=5
i=0
for row in range(0,7):
    for col in range(0,7):
        if (col==1 or ((row==col+1) and col!=0)):
            str=str+"*"
        elif (row==i and col==j):
            str=str+"*"
            i=i+1
            j=j-1
        else:
            str=str+" "
    str=str+"\n"
print(str)