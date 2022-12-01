import pytest
def decor1(cal):
    def cal_enhanced():
        val = cal()
        calculation = val * 5
        return calculation
    return cal_enhanced
def decor(cal):
    def cal_enhanced():
        val1 = cal()
        calculation1 = val1 + 25
        return calculation1
    return cal_enhanced
# @decor
def cal():
    add = 5+20
    return add
cal = decor(decor1(cal))
print(cal())