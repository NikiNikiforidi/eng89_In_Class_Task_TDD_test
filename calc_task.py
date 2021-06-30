# This file (calc_test) contains three methods in the class CalcTest.

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



