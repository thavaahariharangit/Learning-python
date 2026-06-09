class Person:
    def __init_(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)
    
    def stock_price(self):
        total_price = sum(item["price"] for item in self.items)
        return total_price