n=int(input("Enter row number :"))
for i in range(n):
    for j in range(n-i):
        print(j+1, end= ' ')
    print()