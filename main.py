




class Inventory:

    def __init__(self):
        self.Products = {}
    
    def add_item(self, item_name, price, quantity):
        if item_name in self.Products:
            self.Products[item_name]['quantity'] += quantity
        else:
            self.Products[item_name] = {'price': price, 'quantity': quantity}

    def get_item(self, item_name):  
        if item_name not in self.Products:
            print(f"Item '{item_name}' not found in inventory")
        else:
            print(f"Item '{item_name}' found in inventory")

    def list_items(self):
        if not self.Products:
            print("No items in inventory")
        else:
            print("Items in inventory:")
            for item, details in self.Products.items():
                print(f"{item}: Price = {details['price']}, Quantity = {details['quantity']}")
                print(10 * "-----")

    def remove_item(self, item_name, quantity):
        if item_name in self.Products and self.Products[item_name]['quantity'] >= quantity:
            self.Products[item_name]['quantity'] -= quantity
            if self.Products[item_name]['quantity'] == 0:
                del self.Products[item_name]
        else:
            raise ValueError("Item not available or insufficient quantity")
    



    

