class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"
        else:
            return None

    def heal(self, amount):
        self.health = self.health + amount