n = int(input())
heroes = {}
for i in range(n):
    x = input().split(" ")
    if x[0] not in heroes.keys():
        heroes[x[0]] = [x[1], x[2]]

command = input()

while command != "End":
    command = command.split(" - ")
    if command[0] == "CastSpell":
        if int(heroes[command[1]][1]) >= int(command[2]):
            heroes[command[1]][1] = int(heroes[command[1]][1]) - int(command[2])
            print(f"{command[1]} has successfully cast {command[3]} and now has {heroes[command[1]][1]} MP!")
        else:
            print(f"{command[1]} does not have enough MP to cast {command[3]}!")
    if command[0] == "TakeDamage":
        heroes[command[1]][0] = int(heroes[command[1]][0]) - int(command[2])
        if int(heroes[command[1]][0]) > 0:
            print(f"{command[1]} was hit for {command[2]} HP by {command[3]} and now has {heroes[command[1]][0]} HP left!")
        else:
            print(f"{command[1]} has been killed by {command[3]}!")
            heroes.pop(command[1])
    if command[0] == "Recharge":
        x = int(command[2]) + int(heroes[command[1]][1])
        if x >= 200:
            print(f"{command[1]} recharged for {200 - int(heroes[command[1]][1])} MP!")
            heroes[command[1]][1] = 200
        else:
            heroes[command[1]][1] = x
            print(f"{command[1]} recharged for {command[2]} MP!")
    if command[0] == "Heal":
        y = int(command[2]) + int(heroes[command[1]][0])
        if y >= 100:
            print(f"{command[1]} healed for {100 - int(heroes[command[1]][0])} HP!")
            heroes[command[1]][0] = 100
        else:
            heroes[command[1]][0] = y
            print(f"{command[1]} healed for {command[2]} HP!")
    command = input()
t = dict(sorted(heroes.items(), key=lambda s: (-int(s[1][0]), s[0])))
for key, value in t.items():
    print(f"{key}")
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")

