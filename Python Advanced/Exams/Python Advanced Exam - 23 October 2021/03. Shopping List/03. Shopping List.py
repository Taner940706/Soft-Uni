def shopping_list(budget, **kwargs):
    bought = []
    basket = 5
    if budget < 100:
        return 'You do not have enough budget.'
    for item, value in kwargs.items():
        price, quantity = (float(i) for i in value)
        total = price * quantity
        if budget >= total:
            bought.append(f"You bought {item} for {total:.2f} leva.")
            basket -= 1
            budget -= total
            if basket == 0:
                break
    return '\n'.join(bought)

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))