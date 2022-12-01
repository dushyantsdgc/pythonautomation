n=int(input("Enter a number :"))
temp1=n
sum=0
while n>0:
    rem=n%10
    sum=sum+rem**3
    n=n//10

if temp1==sum:
    print("Armstrong")
else:
    print("Not Armstrong")