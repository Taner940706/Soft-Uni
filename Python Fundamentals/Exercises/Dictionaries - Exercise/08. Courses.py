n = input().split(" : ")
a = {}

while n[0] != "end":
    key = n[0]
    if key not in a.keys():
        a[key] = [n[1]]
    else:
        a[key] += [n[1]]
    n = input().split(" : ")

sorted_dict = dict(sorted(a.items(), key=lambda x: -len(x[1])))
for key, value in sorted_dict.items():
    print(f"{key}: {len(value)}")
    for m in sorted(value):
        print(f"-- {m}")
