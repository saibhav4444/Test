class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

a = input("Enter the first number (a): ")
b = input("Enter the second number (b): ")
operation = input("Enter the type of operation (+, -, *, /): ")

calc = Calculator(a, b)

result = None
if operation == '+':
    result = calc.add()
elif operation == '-':
    result = calc.subtract()
elif operation == '*':
    result = calc.multiply()
elif operation == '/':
    result = calc.divide()
else:
    print("Invalid operation!")

if result is not None:
    print("Result:", result)
