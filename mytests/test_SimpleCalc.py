import unittest
import sys
sys.path.append(".")
sys.path.insert(0, '..\\')
from calculator.simplecalculator import Calculator

class TestSimpleCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ("In setupclass() method")
        cls.cal = Calculator(4, 3)

    @classmethod
    def tearDownClass(cls):
        print ("In tearDownClass() method")
        del cls.cal

    def setUp(self):
        print ("In setUp() method")
        self.cal.a = 8
        self.cal.b = 5

    def tearDown(self):
        print("In tearDown() method")
        self.cal.a = 0
        self.cal.b = 0

    def test_simpleadd(self):
        self.assertAlmostEqual(10, self.cal.add(),delta=3)

    def test_simplesub(self):
        self.assertGreater(4, self.cal.sub())

    def test_simplesubFail(self):
        self.assertNotEqual(6, self.cal.sub())


    def test_assertIs_multiply(self):
        self.cal.a = 4
        self.cal.b = 1.2
        self.assertIs(type(1.2), type(self.cal.mul()))

    def test_divison(self):
        self.cal.a = 4
        self.cal.b = 0
        self.assertRaises(ZeroDivisionError, self.cal.div)
        with self.assertRaises(TypeError):
            self.cal1 = Calculator()

if __name__ == '__main__':
    unittest.main()
