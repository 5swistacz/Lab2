import unittest
import Calculator
from Calculator import Calculator
import Exciepcions
from unittest.mock import patch

class TestCalculator(unittest.TestCase):
#Adding tests
    def test_add_integer_should_return_sum(self):
        calculator = Calculator()
        first = 1
        second = 12
        expect_solution = 13
        self.assertEqual(calculator.add(first, second), expect_solution)

    def test_add_string_as_first_argument_should_raise_exepcition_NotANumber(self):
        calculator = Calculator()
        first = 1
        second = 'af'
        self.assertRaises(Exciepcions.NotANumber, calculator.add, first, second)

    def test_add_string_as_second_argument_should_raise_exciepcions_NotANumber(self):
        calculator = Calculator()
        first = 'af'
        second = 2
        self.assertRaises(Exciepcions.NotANumber, calculator.add, first, second)

#Substracting tests
    def test_subtract_integer_should_return_expect_solution(self):
        calculator = Calculator()
        first = 1
        second = 12
        expect_solution = -11
        self.assertEqual(calculator.subtract(first, second), expect_solution)

    def test_subtract_string_as_first_argument_should_raise_exciepcions_NotANumber(self):
        calculator = Calculator()
        first = 1
        second = 'af'
        self.assertRaises(Exciepcions.NotANumber, calculator.subtract, first, second)

    def test_subtract_string_as_second_argument_should_raise_exciepcions_NotANumber(self):
        calculator = Calculator()
        first = 'af'
        second = 2
        self.assertRaises(Exciepcions.NotANumber, calculator.subtract, first, second)

#Derivative tests

    @patch('Calculator.Calculator.derivative')
    def test_derivative(self, mock):
        calculator = Calculator()
        mock.return_value = "e**x"
        function = "e**x"
        order = 30
        expect_solution = "e**x"
        self.assertEqual(expect_solution, str(calculator.derivative(function, order)))




if __name__ == "__main__":
    unittest.main()