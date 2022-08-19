budget = float(input())
people = int(input())
single_outfit_price = float(input())
decor_price = budget * 0.1
outfits_price = people * single_outfit_price
if people > 150:
    outfits_price = outfits_price - (outfits_price * 0.1)
full_sum = decor_price + outfits_price
if full_sum > budget:
    needed_money = full_sum - budget
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")
elif budget >= full_sum:
    money_left = budget - full_sum
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")