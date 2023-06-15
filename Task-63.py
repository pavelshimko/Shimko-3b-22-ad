class Product_card():
    name = 'Soap'
    price = 15
    stock = 15

    def decrease_stock(self):
        self.stock -=1
        if self.stock < 0:
            self.stock = 0
        print(f"Оставшееся количество товара: {self.stock}")

    def change_price(self):
        price_change = 5
        self.price = self.price - price_change
        if self.price < 0:
            self.price = 0
        print(f"Цена равна: {self.price}")

Product_card().change_price()