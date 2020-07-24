
import pytest
from calculator import Calculator, CalculatorError

def test_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5

def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(9, 3)
    assert result == 6

def test_mulitply():
    calculator = Calculator()
    result = calculator.multiply(9, 3)
    assert result == 27

def test_divide():
    calculator = Calculator()
    result = calculator.division(9, 3)
    assert result == 3

# def test_add_weird_stuff():
#     calculator = Calculator()
#     with pytest.raises(CalculatorError) as context:
#         result = calculator.add("two", "three")
#     assert str(context.value) == "random value"

def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.division(9, 0)
