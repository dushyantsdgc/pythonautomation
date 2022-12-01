def test_strReplace():
    string = "Bad, Boys!"
    assert string.replace("Bad", "Good") == "Good, Boys!"


def test_strSplit():
    string = "Hello,World!"
    assert string.split(',') == ["Hello", "World!"]


def test_strStrip():
    string = "Hello World!"
    assert string.strip() == "Hello World!"


def test_strConcat():
    string1 = "Hello"
    string2 = "World"
    assert string1 + string2 == "HelloWorld"
    print("String concat test case has been passed")


def test_strUpper():
    string1 = "python"
    assert string1.upper() == "PYTHON"
    print("Upper test case has been passed")
