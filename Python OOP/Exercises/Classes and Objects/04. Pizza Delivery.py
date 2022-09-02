class PizzaDelivery:

    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = dict(ingredients)

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not PizzaDelivery.ordered:
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] = self.ingredients[ingredient] + quantity
                self.price = self.price + quantity*price_per_quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price = self.price + quantity * price_per_quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients.keys() and (quantity > self.ingredients[ingredient]):
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] = self.ingredients[ingredient] - quantity
            self.price = self.price - quantity*price_per_quantity

    def make_order(self):
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join('{}: {}'.format(key, value) for key, value in self.ingredients.items())} and the price will be {self.price}lv."