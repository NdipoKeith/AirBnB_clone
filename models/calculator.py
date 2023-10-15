class Calculator:
    """class that contain some of the most common maths calculator functions"""

    def __init__(self, x, y):
        """initialization of the class"""
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y != 0:
            return self.x / self.y
        else:
            print("ERROR!!! Try another format")

    def subtract(self):
        return self.x - self.y

    def exponential(self):
        return (self.x ** self.y)

try:
    a = float(input("Enter the first number: "))
    c = input("Enter operation to be made: ")
    b = float(input("Enter the second number: "))
except  EOFError:
    print("EOF error detected!!! exiting program")
    exit()

calculator = Calculator(a, b)

if c == str("+"):
    print(" The sum of numbers: ", calculator.addition())

elif c == str("*"):
    print("The product of numbers: ", calculator.multiply())

elif c == str("/"):
    print("The answer is: ", calculator.divide())
elif c == str("-"):
    print("The answer is: ", calculator.subtract())
elif c == str("**"):
    print("The square is: ", calculator.exponential())
elif c == str("* *"):
    print("The exponential is: ", calculator.exponential())
else:
    raise TypeError("That is a non recognisable operand!!! Try again, please")
