# simple-calculator
I have uploaded two Calculator program using function and class both

Simple Calculator in one Expression:

Through this simple calculator you can perform four operations using 3 inputs. The four operations are

1)Addition 2) Subtraction 3) Multiplication 4) Division 

using fuctions

```python
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

```
using class

```python
class calc:
    def __init__(self, a, b):
        self.num1 = float(a)
        self.num2 = float(b)

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


```
