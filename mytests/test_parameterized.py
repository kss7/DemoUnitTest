import unittest
import sys
sys.path.append(".")
sys.path.insert(0, '..\\')
from calculator.simplecalculator import Calculator
from parameterized import parameterized, parameterized_class


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("In setupclass() method")
        cls.cal = Calculator(0, 0)

    @parameterized.expand([
        (4, -1, 3),
        (-5, -1, -6),
        (3.2, -1.9, 1.3),
    ])
    def test_add_param(self, in1, in2, out):
        self.cal.a = in1
        self.cal.b = in2
        self.assertAlmostEqual(self.cal.add(), out, delta=1)

    @parameterized.expand([
        (4, -1, 5),
        (-5, -1, -4),
        (3.2, -1.9, 5.1),
    ])
    def test_sub_param(self, in1, in2, out):
        self.cal.a = in1
        self.cal.b = in2
        self.assertAlmostEqual(self.cal.sub(), out, delta=1)

if __name__ == '__main__':
    unittest.main()
