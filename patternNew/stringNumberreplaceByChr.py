s="a2b2c3"
outpou=''
for ch in s:
    if ch.isalpha():
        outpou=outpou+ch
        x=ch
    else:
        d=int(ch)
        newc=chr(ord(x)+d)
        outpou=outpou+newc
print(outpou)


