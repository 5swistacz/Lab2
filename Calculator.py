from AbstractCalculator import AbstractCalculator
import Validator
from Validator import InputDataValidator
import sympy
from math import log




class Calculator(AbstractCalculator):
    def __init__(self):
        self._validator = InputDataValidator()

    def add(self, arg1, arg2):
        self._validator.validate(arg1, arg2, 'add')
        return arg1 + arg2

    def subtract(self, arg1, arg2):
        self._validator.validate(arg1, arg2, 'subtract')
        return arg1 - arg2

    def multiple(self, arg1, arg2):
        self._validator.validate(arg1, arg2, 'multiple')
        return arg1 * arg2

    def divide(self, arg1, arg2):
        self._validator.validate(arg1, arg2, 'divide')
        return arg1 / arg2

    def derivative(self, fun, order):
        self._validator.validate(arg1, arg2, 'derivative')
        return sympy.diff(fun, 'x', order)

    def logarithm(self, base, arg):
        self._validator.validate(arg1, arg2, 'logarithm')
        return log(arg, base)