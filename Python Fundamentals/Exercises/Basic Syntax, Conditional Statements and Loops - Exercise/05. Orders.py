n = int(input())
total = 0

for i in range(n):
    price_per_capsule = float(input())
    if price_per_capsule<0.01 or price_per_capsule>100.00:
        continue
    days = int(input())
    if days < 1 or days>31:
        continue
    capsules = int(input())
    if capsules < 1 or capsules > 2000:
        continue
    price = price_per_capsule*days*capsules
    print(f"The price for the coffee is: ${price:.2f}")
    total += price
print(f"Total: ${total:.2f}")
    
    