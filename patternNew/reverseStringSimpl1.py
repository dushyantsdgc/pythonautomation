s=input("Enter some string ")
#r=reversed(s)
#op=''.join(r)
#for ch in r:
#print(op)

output=''
i=len(s)-1
print(i)
while i>=0:
    output=output+s[i]
    i=i-1
print(output)

