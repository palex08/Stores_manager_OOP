class Store():

    def __init__(self, store_name, store_address):
        self.store_name = store_name
        self.store_address = store_address
        self.store_items = {}

    def add_item(self, item_name, item_price):
        self.store_items[item_name] = item_price

    def remove_item(self, item_name):
        del self.store_items[item_name]

    def find_price_of_items(self, item_name):
        return self.store_items.get(item_name)

    def price_update(self, item_name, new_price):
        self.store_items[item_name] = new_price


store1 = Store("Sumbery15", "Verhneportovaya, 15")
store2 = Store("Sumbery14", "Kalinina, 16")
store3 = Store("Sumbery16", "Russkaya, 10")

store1.add_item("milk", 10)
store1.add_item("bread", 15)
store1.add_item("chocolate", 20)

store2.add_item("milk", 10)
store2.add_item("bread", 15)
store2.add_item("chocolate", 20)

store3.add_item("milk", 10)
store3.add_item("bread", 15)
store3.add_item("chocolate", 20)

store2.price_update("milk", 15)
store1.price_update("bread", 20)
store3.price_update("chocolate", 25)

print(store1.store_name, store1.store_address)
for i in store1.store_items:
    print(i, store1.store_items[i])

print(store2.store_name, store2.store_address)
for i in store2.store_items:
    print(i, store2.store_items[i])

print(store3.store_name, store3.store_address)
for i in store3.store_items:
    print(i, store3.store_items[i])

store1.remove_item("milk")
store2.remove_item("bread")
store3.remove_item("chocolate")

print(f'{store1.store_name} bread price {store3.find_price_of_items("bread")}')
print(f'{store2.store_name} milk price {store3.find_price_of_items("milk")}')
print(f'{store3.store_name} chocolate price {store1.find_price_of_items("chocolate")}')
print(f'{store3.store_name} chocolate price {store3.find_price_of_items("chocolate")}')