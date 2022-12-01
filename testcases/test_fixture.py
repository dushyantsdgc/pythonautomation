import pytest


@pytest.fixture
def fixtureMethod():
    print("This is a Fixture Method")


def test_methodA(fixtureMethod):
    print("This is method A")


def test_methodB(fixtureMethod):
    print("This is method B")


def test_methodC(fixtureMethod):
    print("This is method C")


def test_methodD(fixtureMethod):
    print("This is method D")