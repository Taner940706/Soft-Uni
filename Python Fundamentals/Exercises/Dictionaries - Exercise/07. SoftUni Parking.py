n = int(input())
x = {}

for i in range(n):
    a = input().split(" ")
    if a[0] == "register":
        key = a[1]
        if key not in x.keys():
            x[key] = [a[1], a[2]]
            print(f"{x[key][0]} registered {x[key][1]} successfully")
        else:
            print(f"ERROR: already registered with plate number {x[key][1]}")
    if a[0] == "unregister":
        key = a[1]
        if key not in x.keys():
            print(f"ERROR: user {key} not found")
        else:
            print(f"{key} unregistered successfully")
            del x[key]
for key, value in x.items():
    print(f"{key} => {str(value[1])}")
