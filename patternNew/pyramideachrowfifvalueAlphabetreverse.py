n=int(input("Enter number of rows: "))

for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(64-j+n),end=' ')
    print()
for i in range(n-1):
    print(" "*(i+1), end='')
    for j in range(n-i-1):
        print(chr(64-j+n), end=' ')
    print()