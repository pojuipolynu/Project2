import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise Exception('Your numerator is invalid')
        else:
            self.__numerator = numerator
        if not isinstance(denominator, int) or denominator == 0:
            raise Exception('Your denominator is invalid')
        else:
            self.__denominator = denominator

    def __str__(self):
        n = math.gcd(self.__denominator, self.__numerator)
        return f'Fraction: {self.__numerator//n}/{self.__denominator//n}' \
               f'\nDecimal: {self.__numerator/self.__denominator}'


fract = Rational(21, 49)
print(fract.__str__())
