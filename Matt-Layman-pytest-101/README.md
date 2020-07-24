
## Python Testing 101
link:  (Here)[https://youtu.be/etosV2IWBF0]

#### Environment: Native windows python library (3.7)

##### Creating the test file:
The test file has to start with the word “test_” followed by the rest of the name. Same story with the test function name. Has to start with test_.  
##### Example:
We create a test file and call it test_calculator.py and inside it we say:
```python
def test_add():  
Assert True;
```
Then in the command line we say:
```
pytest
```
and we see the test results.![](https://lh3.googleusercontent.com/DIe9IORAZYlkJiEoEpb3dKWUi4FLkPA04rbjOzw_J3PmGsQoy6wDrKTnbCrxKVqFaDcBXhIwPqxzaz2y8afPtw2aPuKiM_tpxUILqZRCicGh7G5p_zYpCH0oW-DZMH2MwVDzZGv8)**
#### Three A concept for testing:
1- Arrange
2- Act
3- Assert
The key to TDD, is to move backwards. For example, we want to create a calculator which has four operators. We can start with saying as the test:
```python
def test_calculator :
    calculator = Calculator()
    result = calculator.add(2, 3)
    Assert result == 5
```
We know this test fails because we didn’t create a Calculator() class. Now, we go and create it, then keep changing the code until the test passes.

For each step we need to develop, actually the test function will tell us what to do. In this example, we first created the class Calculator, then created the method add, etc. until the test passed.

Now, I create a new function to return an error:
```python

def test_add_weird_stuff():
    calculator = Calculator()
    result = calculator.add("two", 3)
    assert result == 5
```
Now we can raise out own exception instead of using python's predefined exceptions.
like this:
```python
def test_add_weird_stuff():
    calculator = Calculator()
    with pytest.raises(calculatorError):
        result = calculator.add("two", 3)
```
(don't forget to import pytest library)

And we need to change our add method to this:
```python
def add(self, a, b):
        try:
            return a + b
        except TypeError:
            raise CalculatorError()
```
Now we need to define CalculatorError() class, like this:
```python
class CalculatorError(Exception):
    '''
    An exception class for calculator
    '''
```
In Python exception we can pass our custom message like this:
```python
def add(self, a, b):
        try:
            return a + b
        except TypeError:
            raise CalculatorError("this is a custom error")
```
What if we pass two strings in add function? the type of the error is not TypeError anymore. we can define a checker method ourself to see if the values are an instance of a builtin "numbers" library in python. like this:
```python
def _check_operand(self, operand):
	if not isinstnce(operand, numbers.Number):
		raise CalculatorError(f'"{operand}" is not a number')
```
This function will check and if we don't pass a number, it will raise the CalculatorError and its message. But we need to call this method inside add method, like this:
```python
def add(self, a, b):
    self._check_operand(a)
    self._check_operand(b)
    return a + b
```
Now it passed the test, which means the error is being raised. And now it is the time to see the value we passed in CaclulatorError(). In order to do this, we use Context Manager like this:

```python
def test_add_weird_stuff():
    calculator = Calculator()
    with pytest.raises(CalculatorError) as context:
        result = calculator.add("two", "three")
	assert str(context.value) == "a random value"
```
This way, the test fails because the value "a random value" is not what we passed. Here is what we get:
>E       assert '"two" is not a real number' == 'random value'
E         - random value
E         + "two" is not a real number






test_calculator.py:29: AssertionError





> Written with [StackEdit](https://stackedit.io/).