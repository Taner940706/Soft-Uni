class Shop:

    def __init__(self, name, items):
        self.name = name
        self.items = items
        
    def get_items_count(self):
        count = 0
        for _ in self.items:
            count += 1
        return count