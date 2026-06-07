class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price          
        })
    
    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
    
    @classmethod
    def franchise(cls, store):
        return cls(f"{store.name} - franchise")
    
    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {store.stock_price()}"
    
store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print(Store.franchise(store).name)
print(Store.franchise(store2).name)

print(Store.store_details(store))
print(Store.store_details(store2))