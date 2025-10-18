
from InventorySystem import Inventory                       

inv = Inventory()

# Create items
inv.create_item("Laptop", 1500.00, 10)
inv.create_item("Smartphone", 800.00, 25)       
inv.create_item("Tablet", 400.00, 15)
inv.create_item("Teclado", 500.00, 10)  # Attempt to add duplicate
inv.create_item("Monitor", 700.00, 20)
inv.create_item("Mouse", 50.00, 100)
inv.create_item("Headphones", 150.00, 30)
inv.create_item("Webcam", 120.00, 40)
inv.create_item("Printer", 200.00, 5)
inv.create_item("Router", 80.00, 50)
inv.create_item("External Hard Drive", 100.00, 15)
inv.create_item("USB Flash Drive", 20.00, 200)
inv.create_item("Speakers", 90.00, 25)
inv.create_item("Microphone", 110.00, 10)   

# Update items
inv.update_item("Laptop", price=1400.00)
inv.update_item("Smartphone", quantity=30)
inv.update_item("Tablet", price=350.00, quantity=20)


# Get item details

inv.list_items()

   