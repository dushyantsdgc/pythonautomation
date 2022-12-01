s="AABBCCFFFSSSFFFSSSSDDDE"
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in d.items():
    print("{} ocuurs {} times".format(k,v))