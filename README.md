# In Class TDD Test Task
### Tasks:
- create a file to write tests. I have named my file tdd_test
- create a file to write code. I have named my file calc_task
- implement sudo coding
- create a README to document the steps to successfully achieve the task

- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test
- create a test case to calculate % and code to pass the test
- create a test to check if the given values are positive 
- create a method in the class to pass the test

### This file is used to test the outcome. tdd_test.py
- Importing and installing below packages

```
import unittest
import pytest

from calc_task import CalcTask

class TDDtest(unittest.TestCase):

    calc = CalcTask()

# This test checks if the input numbers are divisible/ have remainder 0
    def test_divide(self):
        self.assertEqual(self.calc.divide(6,3),True)


# This test checks if the percentage of two numbers are correct
    def test_percentage(self):
        self.assertEqual(self.calc.percentage(1,5),20)


# This test checks if the given values are positive
    def test_positive(self):
        self.assertEqual(self.calc.positive(6,0),True)
```

### This file is used to create calculators. calc_task.py
```
class CalcTask:

    def divide(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def percentage(self, num1, num2):
        if num2 & num2 > 0:
            quotient = num1 / num2
            return quotient * 100
        else:
            return False

    def positive(self, num1, num2):
        if num1 & num2 >= 0:
             return True
        else:
             return False
```

