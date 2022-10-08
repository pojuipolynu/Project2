class Product:
    def __init__(self, price=0, description=None, dimension=None):
        if not isinstance(price, int) or price <= 0:
            raise Exception('Your price is invalid')
        else:
            self.price = price
        self.description = description
        self.dimension = dimension

    def __str__(self):
        return f'Product\nPrice: {self.price}\nDescription: {self.description}\nDimensions: {self.dimension}'


class Customer:
    def __init__(self, name=None, surname=None, patronymic=None, phone=None):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone

    def __str__(self):
        return f'Customer\nSurname and Initials: {self.surname} {self.name[0]}.{self.patronymic[0]} \nPhone number:' \
               f'{self.phone}'


class Order:
    def __init__(self, customer, *args):
        self.customer = customer
        self.product = args

    def total_price(self):
        k = 0
        for x in self.product:
            k += x.price
        return k

    def add_prod(self, a):
        self.product += (a,)

    def del_prod(self, b):
        for a, x in enumerate(self.product):
            if b == x:
                self.product = self.product[:a] + self.product[a+1:]

    def __str__(self):
        k = ''
        for x in self.product:
            k += x.__str__()
        return f'{self.customer}\n{k}'


cus = Customer('Hanna', 'Grych', 'Hryhorivna', '0989823767')
prod1 = (Product(10, 'a', '10'))
prod2 = (Product(13, 'b', '12'))
prod3 = (Product(11, 'c', '15'))
ord1 = Order(cus, prod1, prod2, prod3)
print(ord1.total_price())
ord1.add_prod(prod1)
print(ord1.total_price())
ord1.del_prod(prod2)
print(ord1.total_price())
print(ord1.__str__())
