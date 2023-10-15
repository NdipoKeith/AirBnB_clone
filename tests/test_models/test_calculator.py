#!/usr/in/python3
import unittest
from models.calculator import Calculator 

class TestClass(unittest.TestCase):

    def test_add(self):
        #positive numbers
        calculator = Calculator(10, 5)
        result = calculator.addition()
        self.assertEqual(result, 15)
        #with one negative integer
        calculator = Calculator(-10, 5)
        result = calculator.addition()
        self.assertEqual(result, -5)
        #both negative integers
        calculator = Calculator(-10, -5)
        result = calculator.addition()
        self.assertEqual(result, -15)

    def test_multiply(self):
        calculator = Calculator(10, 5)
        result = calculator.multiply()
        self.assertEqual(result, 50)
        #one negative integer
        calculator = Calculator(-10, 5)
        result = calculator.multiply()
        self.assertEqual(result, -50)
        #both negative integers
        calculator = Calculator(-10, -5)
        result = calculator.multiply()
        self.assertEqual(result, 50)

    def test_divide(self):
        #ensure it isn't dividing bu=y zero
        calculator = Calculator(10, 0)
        result = calculator.divide()
        self.assertRaises(ValueError)

        calculator = Calculator(10, 5)
        result = calculator.divide()
        self.assertEqual(result, 2)
        #one negative integer
        calculator = Calculator(-10, 5)
        result = calculator.divide()
        self.assertEqual(result, -2)
        
        #both negative integer
        calculator = Calculator(-10, -5)
        result = calculator.divide()
        self.assertEqual(result, 2)
    def test_subtract(self):
        calculator = Calculator(10, 5)
        result = calculator.subtract()
        self.assertEqual(result, 5)
        #one negative integer
        calculator = Calculator(-10, 5)
        result = calculator.subtract()
        self.assertEqual(result, -15)
        #both negative integers
        calculator = Calculator(-10, -5)
        result = calculator.subtract()
        self.assertEqual(result, -5)
if __name__ == "__main__":
    unittest.main()
