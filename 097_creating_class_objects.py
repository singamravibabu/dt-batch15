class Product:
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nDiscount percent: {self.discountPercent}\nDiscount amount: {self.getDiscountAmount()}\nDiscount price: {self.getDiscountPrice()}"


watch = Product("FasTrack", 50000.0, 10)
table = Product("Wooden Dining Table", 28000.0, 5)
print(watch)
print(table)