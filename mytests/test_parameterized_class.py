import unittest
import sys
sys.path.append(".")
sys.path.insert(0, '..\\')
from calculator.simplecalculator import Calculator
from parameterized import parameterized, parameterized_class

@parameterized_class(('a', 'b', 'expected_sum', 'expected_sub'), [
   (4, -1, 3, 5),
   (-5, -1, -6, -4),
])
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("In setupclass() method")
        cls.cal = Calculator(0, 0)

    def setUp(self):
        self.cal.a = self.a
        self.cal.b = self.b

    def test_add_param(self):
        self.assertAlmostEqual(self.cal.add(), self.expected_sum, delta=1)

    def test_sub_param(self):
        self.assertAlmostEqual(self.cal.sub(), self.expected_sub, delta=1)

if __name__ == '__main__':
    unittest.main()
