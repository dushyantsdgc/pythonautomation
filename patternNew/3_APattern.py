n=int(input("Enter tge number of row: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j),end=' ')
    print()