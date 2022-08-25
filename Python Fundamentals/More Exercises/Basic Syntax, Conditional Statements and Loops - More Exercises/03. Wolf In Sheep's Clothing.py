animals = input().split(", ");

for i in range(len(animals)):
    if animals[i] == "wolf":
        if i == len(animals) - 1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {len(animals)-i-1}! You are about to be eaten by a wolf!")