class Item:
    rate = 0.8

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def apply_discount(self):
        self.price = self.price * self.rate

item1 = Item("apple", 100)
item1.apply_discount()
# here class levet attribute is used
print(item1.price)

item2 = Item("orange", 100)
item2.rate=0.6
item2.apply_discount()
# here object level attribute is used, cuz we initialized it
print(item2.price)