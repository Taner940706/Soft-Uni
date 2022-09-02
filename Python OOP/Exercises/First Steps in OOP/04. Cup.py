class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        if self.size >= self.quantity + amount:
            self.quantity = self.quantity + amount
        else:
            pass

    def status(self):
        return self.size - self.quantity