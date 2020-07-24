import numbers

class CalculatorError(Exception):
    '''
    An exception class for calculator
    '''
class Calculator:
    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def division(seld, a, b):
        return a / b
    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a real number')
