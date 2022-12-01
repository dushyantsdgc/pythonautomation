s=input("Enter as strinh ")

def reverseString(str1):
    if len(str1)==0:
        return str1
    else:
        return reverseString(str1[1:])+str1[0]




print("Original string ",s)
print("Reverse of string", reverseString(s))