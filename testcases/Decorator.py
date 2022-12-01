import pytest


def decor(cal):
    def cal_enhanced():
        val = cal()
        calculation = val * 5
        return calculation
    return cal_enhanced


@decor
def cal():
    add = 5+20
    return add


# cal = decor(cal)
print(cal())