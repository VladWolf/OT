class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total(self, amount):
        return self.price * amount

class ShoppingCart:
    def __init__(self):
        self.lst = []

    def add(self, product, amount):
        for i in range(amount):
            self.lst.append(product)

    def get_total(self):
        return sum([i.price for i in self.lst])

product = Product("Beer", 32.0)
print(product.get_total(10))

cart = ShoppingCart()
cart.add(product, 2)
print(cart.get_total())

# Волковський Владислав