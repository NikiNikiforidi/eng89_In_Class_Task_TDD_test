# - Importing and installing below packages
# - this file is used to test the outcome

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