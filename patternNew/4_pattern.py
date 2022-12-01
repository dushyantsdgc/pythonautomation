"""
6 6 6 6 6 6
5 5 5 5 5 5
4 4 4 4 4 4
3 3 3 3 3 3
2 2 2 2 2 2
1 1 1 1 1 1

"""


n=int(input("Enter tge number of row: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=' ')
    print()