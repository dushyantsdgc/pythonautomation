#num=int(input("enter a numner :"))
num=32
flag=False
for i in range(2,num):
    if (num%i==0):
        flag=True
        break

if flag:
    print(num,"is not a prime nmber")
else:
    print(num, "is a prime number")