
from InventorySystem import Inventory                       

inv = Inventory()


# Add items
# delete item
inv.remove_item("Notebook", 10)  # remove 5 units
inv.remove_item("Smartphone", 3)  # remove all units                
inv.remove_item("Tablet", 15)  # item does not exist

           

inv.list_items()    