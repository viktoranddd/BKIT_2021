import unittest

from main import get_roots

class TDDtestGetRoots(unittest.TestCase):
	def testGetRoots(self):
		self.assertEqual(get_roots(-4, 16, 0), [-2.0, 0.0, 2.0])
		self.assertEqual(get_roots(1, 1, -2), [-1.0, 1.0])
		self.assertEqual(get_roots(1, 1, 1), [])

if __name__ == "__main__":
	unittest.main()
