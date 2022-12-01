try:
    print("Enter first number")
    x=int(input())
    print("Enter second number")
    y=int(input())
    print(x/y)
except Exception as error:
    print(error)
    print("In except block")
else:
    print("In else block")
finally:
    print("this is always executed")
