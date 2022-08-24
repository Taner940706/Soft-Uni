n = int(input())
b = {}

for i in range(n):
    a = input()
    m = input()
    t = [a, m]
    key = t[0]
    if key not in b.keys():
        b[key] = [float(t[1])]
    else:
        b[key] += [float(t[1])]
sorted_dict = dict(sorted(b.items(), key=lambda x: -sum(x[1])/len(x[1])))
for key, value in sorted_dict.items():
    if sum(value)/len(value) >= 4.50:
        print(f"{key} -> {sum(value)/len(value):.2f}")
