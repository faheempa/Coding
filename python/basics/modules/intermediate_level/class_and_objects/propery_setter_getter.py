class Item:
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0
        assert quantity >= 0

        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self):
        return self.__name

    def set_name(self, value: str):
        self.__name = value

    @property
    def price(self):
        return self.__price

    def set_price(self, value: float):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    def set_quantity(self, value: int):
        self.__quantity = value


class Phone(Item):
    def __init__(self, name, price, quantity, broken=0) -> None:
        assert broken >= 0
        super().__init__(name, price, quantity)
        self.__broken = broken
        self.__unbroken = self.__unbroken_phones()

    @property
    def broken(self):
        return self.__broken

    def set_broken(self, value: int):
        self.__broken = value

    def __unbroken_phones(self):
        return self.quantity - self.__broken

    @property
    def unbroken(self):
        self.__unbroken = self.__unbroken_phones()
        return self.__unbroken


phone1 = Phone("htc", 10000, 343, 56)

print(phone1.name)
print(phone1.price)
print(phone1.broken)
print(phone1.unbroken)

phone1.set_name("vivo")
phone1.set_price(15000)
phone1.set_broken(29)

print()
print(phone1.name)
print(phone1.price)
print(phone1.broken)
print(phone1.unbroken)

