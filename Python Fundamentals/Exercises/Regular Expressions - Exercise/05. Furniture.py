import re

pattern = '^>>([A-Za-z]+)<<(\d+\.?\d*)\D(\d+)$'
bought_furniture = []
total_sum = 0
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_sum += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_sum:.2f}")


