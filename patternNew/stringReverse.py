#s=input("Enter string :")
#print(''.join(reversed(s)))
#print(''.join(reversed(s)))

#s="shyamg"
#print(s[::-1])

s=input("Enter a string")
x=s
n=len(s)-1
target=''
while n>=0:
    target=target+s[n]
    n=n-1
print(target)
if x==s:
    print("palindrome")
else:
    print("not palindrome")