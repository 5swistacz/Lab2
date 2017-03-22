from abc import ABC, abstractmethod

class AbstractCalculator(ABC):

    @abstractmethod
    def add(self, arg1, arg2):
        pass

    @abstractmethod
    def subtract(self, arg1, arg2):
        pass

    @abstractmethod
    def multiple(self, arg1, arg2):
        pass

    @abstractmethod
    def divide(self, arg1, arg2):
        pass

    @abstractmethod
    def derivative(self, fun, order):
        pass

    @abstractmethod
    def logarithm(self, arg1):
        pass

