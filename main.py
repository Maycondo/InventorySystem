
from InventorySystem import Inventory                       

inv = Inventory()


# Add items
inv.create_item("Notebook", 1500.00, 10)  # add 10 units
inv.create_item("Smartphone", 800.00, 3)  # add 3 units
inv.create_item("Tablet", 400.00, 5)  #
inv.create_item("Headphones", 150.00, 15)  # add 15 units
inv.create_item("Smartwatch", 200.00, 7)  # add 7 units
inv.create_item("Smartphone", 800.00, 2)  # add 2 more units

# Remove items
inv.remove_item("Headphones", 5)  # remove 5 units      
inv.remove_item("Notebook", 12)  # try to remove 12 units (only 10 available)
inv.remove_item("Tablet", 10)  # try to remove 10 units (only 5 available)
inv.remove_item("Smartphone", 1)  # remove 1 unit   
inv.remove_item("Smartwatch", 3)  # remove 3 units # remove 3 units 


inv.list_items()    