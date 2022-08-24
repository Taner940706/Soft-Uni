n = input().split(" -> ")
a = {}

while n[0] != "End":
    key = n[0]
    if key not in a.keys():
        a[key] = [n[1]]
    else:
        a[key] += [n[1]]
    n = input().split(" -> ")

sorted_dict = dict(sorted(a.items(), key=lambda x: (x[0])))
for key, value in sorted_dict.items():
    print(f"{key}")
    value = list(dict.fromkeys(value))
    for m in value:
        print(f"-- {m}")
