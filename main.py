


class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, price, quantity):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def get_item(self, item_name):
        return self.items.get(item_name, None)
    
    def list_items(self):
        return self.items

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name]['quantity'] >= quantity:
            self.items[item_name]['quantity'] -= quantity
            if self.items[item_name]['quantity'] == 0:
                del self.items[item_name]
        else:
            raise ValueError("Item not available or insufficient quantity")
    

    

    

