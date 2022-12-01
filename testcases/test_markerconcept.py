import pytest
@pytest.mark.login
def test_strReplace():
    string = "Hello, World!"
    assert string.replace("H","J") == 'Jello, World!'

@pytest.mark.skip
def test_strSplit():
    string="Hello,World!"
    assert string.split(',')==["Hello","World!"]

@pytest.mark.xfail
def test_strStrip():
    string ="Hello World!  "
    assert string.strip()=="Hello World!"

@pytest.mark.skipif(reason="xyz")
def test_strConcat():
    string1="Hello"
    string2="World"
    assert string1+string2=="HelloWorld"

@pytest.mark.login
def test_strUpper():
    string1="python"
    assert string1.upper()=="PYTHON"
    print("\nLast wlal")