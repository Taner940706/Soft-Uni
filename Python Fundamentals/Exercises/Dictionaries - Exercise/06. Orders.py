n = input().split(" ")
a = {}
b = {}
while n[0] != "buy":
    key = n[0]
    if key not in a.keys():
        a[key] = [n[1], n[2]]
    else:
        a[key][1] = int(a[key][1]) + int(n[2])
        if a[key][0] != n[1]:
            a[key][0] = n[1]
    b[key] = float(a[key][0])*int(a[key][1])
    n = input().split(" ")

for key, value in b.items():
    print(f"{key} -> {float(value):.2f}")
