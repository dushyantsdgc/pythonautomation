try:
    print("Enter first number ")
    x = int(input())
    print("Enter second number ")
    y = int(input())
    if y==0:
        raise Exception("Y can't be zero!!")
    print(x / y)
except Exception as e:
    print(e)
