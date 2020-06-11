
class Employee:
    __empCount = 0

    def __init__(self, eid=None, name=None, salary=None):
        if eid is not None:
            self.__eid = eid
            self.__name = name
            self.__salary = salary
            Employee.__empCount += 1

    def getCount(self):
        return Employee.__empCount

    def getSalary(self):
        return self.__salary

    def getEmployee(self):
        print("eid : ", self.__eid, ", Name : ", self.__name, ", Salary: ", self.__salary)


class EmpDetails:
    def __init__(self, emp=None):
        self.emp = emp or Employee()
        self.high_employee = 1000
        self.low_employee = 100

    def checkTotalEmployee(self):
        count = self.emp.getCount()
        if count > self.high_employee:
            return 'Too congested'
        elif count < self.low_employee:
            return "Feeling lonely"
        else:
            return "All good"


if __name__ == '__main__':
    emp1 = Employee(1, 'King', 120)
    emp2 = Employee(2, 'Lisa', 988)
    emp3 = Employee(3, 'Rey', 902)
    empdetail = EmpDetails()
    print(empdetail.checkTotalEmployee())
    print(emp3.getCount())