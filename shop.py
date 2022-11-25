class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_total(self, amount):
        return round(self.price * amount, 2) # round((self.price * 100)*amount /100, 2)
    
class ShoppingCart:
    def __init__(self):
        self.goods_quantities = []
        self.purchases = []

    def add(self, product, amount):
        self.purchases.append(product)
        self.goods_quantities.append(amount)
    
    def get_total(self):
        total = 0
        for product, amount in zip(self.purchases, self.goods_quantities):
            total += product.get_total(amount)
        
        return round(total, 2)

product = Product("Beer", 32.23)
print(product.get_total(12))

cart = ShoppingCart()
cart.add(product, 4)
print(cart.get_total())

# Волковський Владислав