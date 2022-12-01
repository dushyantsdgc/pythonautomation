import pytest


@pytest.mark.parametrize("x", (1, 2, 3))
def test_parameterMethod1(x):
    print("This is a parametrized Method_1", x)


@pytest.mark.parametrize("x,y", ((1,2),(4,5)))
def test_parameterMethod2(x,y):
    print("This is a parametrized Method_2", x+y)