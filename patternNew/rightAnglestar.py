n=int(input("Enter number of row : "))
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-j), end=' ')
    print()


