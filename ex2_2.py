import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator
        self.frac_sco()

    def frac_sco(self):
        if isinstance(self.__numerator, int) and isinstance(self.__denominator, int):
            n = math.gcd(self.__denominator, self.__numerator)
            self.__numerator = self.__numerator // n
            self.__denominator = self.__denominator // n
        else:
            print('Your variables (or one of them) are invalid')

    def print_drib(self):
        if self.__denominator == 1:
            fraction = self.__numerator
        else:
            fraction = f'{self.__numerator}/{self.__denominator}'
        return fraction

    def print_ddrib(self):
        fraction = self.__numerator/self.__denominator
        return fraction


fract = Rational(2, 4)
print(fract.print_drib())
print(fract.print_ddrib())
