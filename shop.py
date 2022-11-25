class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_total(self, amount):
        return round(self.price * amount, 2) # round((self.price * 100)*amount /100, 2)
    
class ShoppingCart:
    def __init__(self):
        self.purchases = []
        self.goods_price = []

    def add(self, product, amount):
        goods = [product for i in range(amount)]
        self.goods_price.append(product.price*amount)
        self.purchases.append(goods)
    
    def get_total(self):
        return round(sum(self.goods_price), 2)

product = Product("Beer", 32.23)
print(product.get_total(12))

cart = ShoppingCart()
cart.add(product, 4)
print(cart.purchases)
print(cart.get_total())

# Волковський Владислав