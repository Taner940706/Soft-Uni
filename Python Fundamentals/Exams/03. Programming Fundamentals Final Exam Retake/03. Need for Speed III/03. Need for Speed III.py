number_cars = int(input())
cars = {}

for i in range(number_cars):
    new_car = input().split("|")
    if new_car[0] not in cars:
        cars[new_car[0]] = [new_car[1], new_car[2]]

command = input()

while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        a = int(command[2])
        b = int(command[3])
        c = int(cars[command[1]][0])
        d = int(cars[command[1]][1])
        if d > b:
            cars[command[1]] = [(a+c), (d-b)]
            print(f"{command[1]} driven for {a} kilometers. {b} liters of fuel consumed.")
            if cars[command[1]][0] > 100000:
                element = cars.pop(command[1])
                print(f"Time to sell the {command[1]}!")
        else:
            print("Not enough fuel to make that ride")
    if command[0] == "Refuel":
        a = int(command[2])
        if (int(cars[command[1]][1]) + a) >= 75:
            cars[command[1]][1] = 75
        else:
            cars[command[1]][1] = int(cars[command[1]][1]) + a
        print(f"{command[1]} refueled with {a} liters")
    if command[0] == "Revert":
        a = int(command[2])
        x = int(cars[command[1]][0]) - a
        cars[command[1]][0] = x
        if x > 10000:
            print(f"{command[1]} mileage decreased by {a} kilometers")
        else:
            x = 10000
            cars[command[1]][0] = x
    command = input()
t = dict(sorted(cars.items(), key=lambda s: (-int(s[1][0]), s[0])))
for key, value in t.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
