import unittest
import math

from AreaPerimCircum import *

apc = AreaPerimCircum()

class TestAreaPerimCircum(unittest.TestCase):

	def test_validShapeInput(self):
		self.assertEqual(apc.invalid(), "Invalid shape selection!", "test_validShapeInput should say invalid shape selection")

	def test_rectangle(self):
		self.assertEqual(apc.rectangle(6, 7), [42, 26], "input of l=6, w=7 into rectangle should output [42,26]")
		self.assertEqual(apc.rectangle(2, 4), [8, 12], "input of l=2, w=4 into rectangle should output [8,12]")

	def test_square(self):
		self.assertEqual(apc.square(7), [49, 28], "input of s=7 into square should output [49, 28]")
		self.assertEqual(apc.square(12), [144, 48], "input of s=12 into square should output [144, 48]")

	def test_circle(self):
		self.assertEqual(apc.circle(3), [math.pi*9, math.pi*6], "input of r=3 into circle should output [pi*9, pi*6]")
		self.assertEqual(apc.circle(9), [math.pi*81, math.pi*18], "input of r=9 into circle should output [pi*81, pi*18]")

if __name__ == "__main__":
    unittest.main()