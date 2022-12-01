num = int(input("Enter a number :"))
rev_num = 0
def reverseRecusion(num1):
    global rev_num
    if (num1>0):
        rem=num1%10
        rev_num=(rev_num*10)+rem
        reverseRecusion(num1//10)
    return rev_num



rev_num=reverseRecusion(num)
print("Reverse a number {}".format(rev_num))