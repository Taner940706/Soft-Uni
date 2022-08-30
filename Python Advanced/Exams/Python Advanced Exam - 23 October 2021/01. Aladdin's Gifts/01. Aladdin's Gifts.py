from collections import deque as dq

materials = [int(i) for i in input().split()]
magic_levels = dq(int(i) for i in input().split())

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0

}

while materials and magic_levels:
    material = materials[-1]
    magic = magic_levels[0]

    result = material + magic

    if result < 100:
        if result % 2 == 0:
            result = material * 2 + magic * 3
        else:
            result *= 2
    elif result > 499:
        result /= 2

    if 100 <= result <= 199:
        gifts['Gemstone'] += 1

    elif 200 <= result <= 299:
        gifts['Porcelain Sculpture'] += 1

    elif 300 <= result <= 399:
        gifts['Gold'] += 1

    elif 400 <= result <= 499:
        gifts['Diamond Jewellery'] += 1

    materials.pop()
    magic_levels.popleft()

if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or \
        (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    print(f'The wedding presents are made!')
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(i) for i in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(i) for i in magic_levels)}")

for k, v in sorted(gifts.items()):
    if v > 0:
        print(f'{k}: {v}')
