import unittest

from main import summa
from main import raznost
from main import proizv
from main import chastnoe

class TDDtestFunc(unittest.TestCase):
    def testFunc(self):
        self.assertEqual(summa(3, 2), 5)
        self.assertEqual(raznost(3, 2), 1)
        self.assertEqual(proizv(3, 2), 6)
        self.assertEqual(chastnoe(3, 2), 1.5)

if __name__ == "__main__":
    unittest.main()