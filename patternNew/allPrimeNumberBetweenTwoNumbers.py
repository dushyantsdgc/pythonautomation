lower=1   #int(input("Enter initial number"))
upper=100     #int(input("Enter Last number"))

for num in range(lower,upper+1):
    if num >=1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)
