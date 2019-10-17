import unittest
from StringMultiplication import StringMultiplication


sm = StringMultiplication()

class TestStringMultiplication(unittest.TestCase):

    def test_multiplicationOf12and11(self):
        self.assertEqual(sm.multiply("12","11"), "132", "Multiplication of '12' and '11' returns '132'")
    
    def test_thatStringsOnly(self):
        self.assertEqual(sm.multiply(12,11), "Strings only accepted", "Multiplication of non strings will return error message")

    def test_multiplicationof25and25(self):
        self.assertEqual(sm.multiply("25","25"), "625", "Multiplication of '25' and '25' returns '625'")

if __name__ == "__main__":
    unittest.main()