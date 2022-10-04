class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def get_var(self):
        return self.length, self.width

    def set_var(self, a, b):
        if isinstance(a, float) and (0.0 < a < 20.0) and isinstance(b, float) and (0.0 < b < 20.0):
            self.length = a
            self.width = b
        else:
            print('Your variables (or one of them) are invalid')

    def perimeter(self):
        return self.length + self.width

    def area(self):
        return self.length * self.width


figure = Rectangle()
figure.set_var(10.0, 22.3)
print('Area: ', figure.area(), '| Perimeter: ', figure.perimeter())






