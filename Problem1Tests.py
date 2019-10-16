import unittest
from Problem1 import * 

problem1 = Problem1()

class TestProblem1(unittest.TestCase):
    
    def test_returnType(self):
        self.assertTrue(type(problem1.urlSplit("a://b/c")) is list, "test_returnType should return a list of strings")

    def test_inputWithAllComponents(self):
        self.assertEqual(problem1.urlSplit("https://www.google.com/some-path"), ["https", "www.google.com", "some-path"], "test_returnType should return all its components: http, www.google.com, some-path")
    
    def test_inputWithPathMissing(self):
        self.assertEqual(problem1.urlSplit("ftp://bu.edu/"), ["ftp", "bu.edu", ""], "test_returnType should return all its components: ftp, bu.edu, "" ")
    

if __name__ == "__main__":
    unittest.main()
