
def factorailR(number):
    if number <0:
        return 0
    elif number==1:
        return 1
    else:
        return number*factorailR(number-1)




num=int(input("Enter a number :"))
fact=factorailR(num)
print("Factorail of ",num, "is",fact)