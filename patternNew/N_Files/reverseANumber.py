num=int(input("Enter a number"))

palindrome1=num
rev=0
while num>0:
    remainder=num%10
    rev=rev*10+remainder
    num=num//10

print("Reverse a number {}".format(rev))

if rev==palindrome1:
    print("Palindrome")
else:
    print("Not palindrome")



