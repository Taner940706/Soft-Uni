from collections import deque

effects = deque(int(i) for i in input().split(", "))
powers = [int(i) for i in input().split(", ")]

palm_effect = 0
willow_effect = 0
crossette_effect = 0

while True:
    if not effects or not powers:
        break

    if palm_effect >= 3 and willow_effect >= 3 and crossette_effect >= 3:
        break

    effect = effects[0]
    power = powers[-1]

    if effect <= 0:
        effects.popleft()
        continue
    if power <= 0:
        powers.pop()
        continue

    result = effect + power

    if result % 3 == 0 and result % 5 != 0:
        palm_effect += 1
        effects.popleft()
        powers.pop()
    elif result % 5 == 0 and result % 3 != 0:
        willow_effect += 1
        effects.popleft()
        powers.pop()
    elif result % 5 == 0 and result % 3 == 0:
        crossette_effect += 1
        effects.popleft()
        powers.pop()
    elif result % 5 != 0 and result % 3 != 0:
        effect = effect - 1
        effects.popleft()
        effects.append(effect)


if palm_effect >= 3 and willow_effect >= 3 and crossette_effect >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print(f"Firework Effects left: {', '.join(str(i) for i in effects)}")
if powers:
    print(f"Explosive Power left: {', '.join(str(i) for i in powers)}")

print(f"Palm Fireworks: {palm_effect}")
print(f"Willow Fireworks: {willow_effect}")
print(f"Crossette Fireworks: {crossette_effect}")
