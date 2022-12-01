def factorial(num):
    factorial=1
    if num <0:
        print("no factorrial for less thane zero")
    elif num==0:
        print("factorial of zero is 1")
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print("factoral of ",num, "is", factorial)

n=int(input("Enter a  number :"))
factorial(n)