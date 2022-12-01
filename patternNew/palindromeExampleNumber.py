n=int(input("Enter a number :"))

temp1_Pali=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp1_Pali==rev:
    print("Palindrome")
else:
    print("Not Palindrome")