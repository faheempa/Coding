import csv

class Item:
    # class attribute
    all = []

    @classmethod
    def make_object_from_csv_file(cls):
        with open("data.csv", "r") as data:
            read = list(csv.DictReader(data))

        for d in read:
            a = d.get("name")
            b = int(d.get("price"))
            c = float(d.get("quantity"))
            Item(a, b, c)

    def __init__(self, name: str, price: float, quantity=0):

        assert price >= 0, "price is less than 0"
        assert quantity >= 0, "quantity is less than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.name}"


Item.make_object_from_csv_file()

print(Item.all)
