n=int(input("Enter number of row : "))
for i in range(n):
    print(' '*(n-i-1), end=' ')
    for j in range(i+1):
        print(chr(65+n-j), end=' ')
    print()