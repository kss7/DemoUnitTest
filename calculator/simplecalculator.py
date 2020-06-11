class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

    def add2(self, a, b):
        return a + b



if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    obj = Calculator(a, b)
    choice = 1

    while choice != 0:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Result: ", obj.add())
        elif choice == 2:
            print("Result: ", obj.sub())
        elif choice == 3:
            print("Result: ", obj.mul())
        elif choice == 4:
            print("Result: ", round(obj.div(), 2))
        elif choice == 0:
            print("Exiting!")
        else:
            print("Invalid choice!!")