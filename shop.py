class Product:
    def __init__(self, name='', price=''):
        self.name = name
        self.price = price

    def get_total(self, amount):
        return round(self.price * amount, 3)
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
    
    def __float__(self):
        return self.price
    
    def __str__(self):
        return self.name

class ShoppingCart:
    def __init__(self):
        self.goods_quantities = []
        self.purchases = []

    def add_product(self, product, amount):
        if product not in self.purchases:
            self.purchases.append(product)
            self.goods_quantities.append(amount)
        else:
            product_ind = self.purchases.index(product)
            self.goods_quantities[product_ind] = round(self.goods_quantities[product_ind] + amount, 2)

    def get_total(self):
        total = 0
        for product, amount in zip(self.purchases, self.goods_quantities):
            total += product.get_total(amount)
        
        return round(total, 2)

    def __repr__(self):
        return (f"Your cart contains {list(zip(self.purchases, self.goods_quantities))}")
    
    def __float__(self):
        return self.get_total()
    
    def __add__(self, other):
        if isinstance(other, Product):
            self.add_product(other, 1)
            return self
        elif isinstance(other, ShoppingCart):
            new_obj = ShoppingCart()
            for product, amount in zip(self.purchases + other.purchases, self.goods_quantities + other.goods_quantities):
                new_obj.add_product(product, amount)           
        return new_obj

apple = Product()
apple.name = "apple"
apple.price = 10.59
juice = Product()
juice.name = "juice"
juice.price = 36.55
apple_2 = Product('apple', 10.59)
peach = Product('peach')

print(apple == apple_2)
print(float(apple_2))
print(str(apple_2))


obj = ShoppingCart()
obj.add_product(apple, 0.35)
obj.add_product(juice, 4)
obj.add_product(apple, 0.35)

print(float(obj))

assert obj.get_total() == 153.61

print(obj.purchases, obj.goods_quantities)

obj = obj + peach # добавление продукта
print(obj.__dict__) 

new_obj = ShoppingCart()
new_obj.add_product(apple, 0.35)
new_obj.add_product(juice, 4)
new_obj.add_product(peach, 1)

obj = obj + new_obj # корзины
print(obj.__dict__)

#Волковський Владислав