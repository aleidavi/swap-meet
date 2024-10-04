from swap_meet.item import Item
class Electronics(Item):
    '''
    Represents an electronic item with a type attribute.
    Inherits from Item
    '''
    
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
    def get_category(self):
        return "Electronics"
        
