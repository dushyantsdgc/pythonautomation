n=int(input("Enter the length "))
n1=0
n2=1
count=0
if n<=0:
    print("Please eneter a positive  number, emetered number is not valid")
elif n==1:
    print("Fibbonacci series up to ",n, ":")
    print(n1)
else:
    print("Fibbonacci series of the number is")
    while count < n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
