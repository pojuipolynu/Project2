class Product:
    def __init__(self, price=None, description=None, dimension=None):
        self.price = price
        self.description = description
        self.dimension = dimension


class Customer:
    def __init__(self, name=None, surname=None, patronymic=None, phone=None):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone


class Order:
    def cus_sum(self, c):
        k = f'Customer: {c.surname} {c.name[0]}.{c.patronymic[0]}.\nPhone number: {c.phone}'
        return k

    def total_price(self, prodlist):
        k = 0
        for x in prodlist:
            k += x.price
        return k

    def print_list(self, prodl):
        k = ''
        for x in prodl:
            k += f'{x.price} {x.description} {x.dimension}\n'
        return k


cus = Customer('Anna', 'Lin', 'Hryhorivna', '0989823767')
prod3 = []
prod3.append(Product(10, 'a', '10'))
prod3.append(Product(13, 'b', '12'))
prod3.append(Product(11, 'c', '15'))
ord1 = Order()
print(f'{ord1.cus_sum(cus)}\nProducts(price, description, dimension);\n{ord1.print_list(prod3)}'
      f'Total: {ord1.total_price(prod3)}')
