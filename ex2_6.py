class BinaryTree:

    def __init__(self, code1, price):
        self.left = None
        self.right = None
        self.code1 = code1
        self.price = price

    def insert(self, code2, price):
        if self.code1:
            if code2 < self.code1:
                if self.left is None:
                    self.left = BinaryTree(code2, price)
                else:
                    self.left.insert(code2, price)
            elif code2 > self.code1:
                if self.right is None:
                    self.right = BinaryTree(code2, price)
                else:
                    self.right.insert(code2, price)
        else:
            self.code1 = code2
            self.price = price

    def tot_price(self, code3, quantity1):
        if code3 < self.code1:
            if self.left is None:
                return f'There is not such product'
            return self.left.tot_price(code3, quantity1)
        elif code3 > self.code1:
            if self.right is None:
                return f'There is not such product'
            return self.right.tot_price(code3, quantity1)
        else:
            return f'Total price of product is {self.price*quantity}'

    def print_prod(self):
        if self.left:
            self.left.print_prod()
        print(f'\nCode of the product: {self.code1}\nPrice of the product: {self.price}'),
        if self.right:
            self.right.print_prod()


root = BinaryTree(2237, 50)
root.insert(1413, 34)
root.insert(3375, 12)
root.insert(3211, 14)
root.print_prod()
print("\nEnter the code of product:")
code = int(input())
print("Enter the quantity of product:")
quantity = int(input())
print(root.tot_price(code, quantity))
