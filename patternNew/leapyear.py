y=int(input("Enter a year :"))

if (y%400==0) and (y%100==0):
    print("{0} Leap Year".format(y))
#elif (y%4==0) and (y%100!=0):
#    print("{0} is leap year".format(y))
else:
    print("{0} is not a leap year".format(y))