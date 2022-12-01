import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary


    def setUp(self):
    #     ... code to execute in preparation for tests ...

    def tearDown(self):
    #     ... code to execute to clean up after tests ...

    def test_feature_one(self):
        # Test feature one.
        assert 5 == 5

    def test_feature_two(self):
        # Test feature two.
        assert 3 == 3


class MyTestCase2(unittest.TestCase):

    def test_feature_one(self):
        # Test feature one.
        assert 'a' == 'a'

    def test_feature_two(self):
        # Test feature two.
        assert "Dushyant" == "Dushyant"

#... more test classes ...

if __name__ == '__main__':
    unittest.main()