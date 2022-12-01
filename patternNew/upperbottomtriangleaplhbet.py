n=int(input("Enter number of rows: "))
for i in range(n):
    print((chr(65+i)+" ")*(i+1))
for i in range(n-1):
    print((chr(63+n-i)+" ")*(n-i-1))
