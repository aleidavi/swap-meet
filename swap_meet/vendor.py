
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def __contains__(self, item):
        # return self.inventory[0] <= item <= self.inventory[len(self.inventory-1)]
        return item in self.inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item

    
    def remove(self, item):
         
        if item not in self.inventory:
            return False
    
        else:
            self.inventory.remove(item)
            return item

    def get_by_id(self, vendor_id):
        
        # return Item object inside the inventory list
        # whose id matches the vendor id
        for item in self.inventory:
            if vendor_id == item.id:
                return item
            
        return None
                
        
    def swap_items(self, other_vendor, my_item, their_item):
        my_item_remove = self.remove(my_item)
        their_item_remove = self.remove(their_item)

        if not my_item_remove or not their_item_remove:
            return False
        
        elif my_item_remove == my_item and their_item_remove == their_item:
            self.add(their_item)
            other_vendor.add(my_item)

    def new_method(self, their_item):
        self.add(their_item)



        


