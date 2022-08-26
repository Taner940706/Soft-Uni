from operator import add
command_1 = input()
towns = {}
while command_1 != "Sail":
    command_1 = command_1.split("||")
    a = command_1[0]
    b = int(command_1[1])
    c = int(command_1[2])
    if a not in towns.keys():
        towns[a] = [b, c]
    else:
        l = [x + y for x, y in zip(towns[a], [b, c])]
        towns[a] = l
    command_1 = input()
command_2 = input()

while command_2 != "End":
    command_2 = command_2.split("=>")
    if command_2[0] == "Plunder":
        print(f"{command_2[1]} plundered! {command_2[3]} gold stolen, {command_2[2]} citizens killed.")
        if command_2[1] in towns.keys():
            l = [x - y for x, y in zip(towns[command_2[1]], [int(command_2[2]), int(command_2[3])])]
            towns[command_2[1]] = l
        if towns[command_2[1]][0] <= 0 or towns[command_2[1]][1] <= 0:
            print(f"{command_2[1]} has been wiped off the map!")
            towns.pop(command_2[1])
    if command_2[0] == "Prosper":
        if int(command_2[2]) < 0:
            print("Gold added cannot be a negative number!")
        else:
            if command_2[1] in towns.keys():
                l = [x + y for x, y in zip(towns[command_2[1]], [0, int(command_2[2])])]
                towns[command_2[1]] = l
                print(f"{command_2[2]} gold added to the city treasury. {command_2[1]} now has {towns[command_2[1]][1]} gold.")
    command_2 = input()
if len(towns.keys()) > 0:
    print(f"Ahoy, Captain! There are {len(towns.keys())} wealthy settlements to go to:")
    t = dict(sorted(towns.items(), key=lambda x: (-int(x[1][1]), x[0])))
    for key, value in t.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
