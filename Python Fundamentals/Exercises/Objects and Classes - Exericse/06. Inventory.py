class Inventory:
    items = []
    def __init__(self, __capacity):
        self.__capacity = __capacity
    def add_item(self, item: str):
        if len(Inventory.items) < self.__capacity:
            Inventory.items.append(item)
        else:
            return "not enough room in the inventory"
    def get_capacity(self):
        return self.__capacity
    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {self.get_capacity() - len(Inventory.items)}"