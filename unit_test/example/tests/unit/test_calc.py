import unittest
# import the module that contains the class to be tested
from mycalc.calc import Calculator

# run at the beginning of the module test codes
def setUpModule():
    pass

# run at the end of the module test codes
def tearDownModule():
    pass

# test class starts with Test*
class TestCalculator(unittest.TestCase):

    # method called to prepare the test fixture
    # called immediately before calling the test method
    def setUp(self):
        self.cal = Calculator()

    # called immediately after the test method has been called and the result recorded
    # called even if the test method raised an exception
    def tearDown(self):
        self.cal = None

    # a class method called before any test run
    @classmethod
    def setUpClass(cls):
        pass

    # a class method called after all the tests have run
    @classmethod
    def tearDownClass(cls):
        pass

    # all test functions start with test_*
    def test_mod_with_remainder(self):
        self.assertEqual(self.cal.mod(5, 3), (1, 2))

    def test_mod_without_remainder(self):
        self.assertEqual(self.cal.mod(8, 4), (2, 0))

    def test_mod_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as cm:
            self.cal.mod(7, 0)

#if __name__ == '__main__':
#    unittest.main()
