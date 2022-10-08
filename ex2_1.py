class Rectangle:
    def __init__(self, length=1, width=1):
        if not isinstance(length, float) and not isinstance(length, int) or not 0 < length < 20:
            raise Exception('Your variables (or one of them) are invalid')
        else:
            self.length = length
        if not isinstance(width, float) and not isinstance(width, int) or not 0 < width < 20:
            raise Exception('Your variables (or one of them) are invalid')
        else:
            self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def perimeter(self):
        return self.length*2 + self.width*2

    def area(self):
        return self.length * self.width

    def set_length(self, a):
        if not isinstance(a, float) and not isinstance(a, int) or not 0 < a < 20:
            raise Exception('Your variables (or one of them) are invalid')
        else:
            self.length = a

    def set_width(self, a):
        if not isinstance(a, float) and not isinstance(a, int) or not 0 < a < 20:
            raise Exception('Your variables (or one of them) are invalid')
        else:
            self.width = a


figure = Rectangle(2, 12)
print('Area: ', figure.area(), '| Perimeter: ', figure.perimeter())
figure.set_length(13)
figure.set_width(15)
print('Area: ', figure.area(), '| Perimeter: ', figure.perimeter())




