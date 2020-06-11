import unittest
from unittest.mock import MagicMock, patch, Mock
from employee.Employee import Employee, EmpDetails
import employee.Employee

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.emp1 = Employee(1, 'Sam', 3500)
        cls.emp2 = Employee(2, 'Joey', 2200)

    def setUp(self):
        self.empDetails = EmpDetails()

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

    def test_employee(self):
        sal1 = self.emp1.getSalary()
        self.assertEqual(sal1, 3500)

    def test_emp_details(self):
        emp = Employee()
        #print (emp.getCount())
        #print (self.empDetails.checkTotalEmployee())
        self.assertEqual(self.empDetails.checkTotalEmployee(), "Feeling lonely")

    @patch('employee.Employee.Employee')
    def test_empcount_with_mock(self, MockEmp):
        emp = MockEmp()
        emp.getCount.return_value = 155
        self.emp_detail = EmpDetails(emp)
        #print (emp.getCount())
        #print(self.emp_detail.checkTotalEmployee())
        self.assertEqual(self.emp_detail.checkTotalEmployee(), "All good")

    def test_with_magicmock(self):
        emp = Employee()
        emp.getCount = MagicMock(return_value=1500)
        print(emp.getCount())
        self.empdetail = EmpDetails(emp)
        self.assertEqual(self.empdetail.checkTotalEmployee(), "Too congested")

if __name__ == '__main__':
    unittest.main()
