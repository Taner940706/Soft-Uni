bitcoins = 0
health = 100
br = 0
rooms = input().split("|")

for i in rooms:
    i = i.split(" ")
    br = br + 1
    if i[0] == "potion":
        k = int(i[1])
        if (health + k) <= 100:
            health = health + k
            print(f"You healed for {k} hp.")
            print(f"Current health: {health} hp.")
        elif (health + k) > 100:
            print(f"You healed for {100-health} hp.")
            health = 100
            print(f"Current health: {health} hp.")
    elif i[0] == "chest":
        s = int(i[1])
        bitcoins = bitcoins + s
        print(f"You found {s} bitcoins.")
    else:
        m = int(i[1])
        health = health - m
        if health <= 0:
            print(f"You died! Killed by {i[0]}.")
            print(f"Best room: {br}")
            break
        else:
            print(f"You slayed {i[0]}.")
if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
