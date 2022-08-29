text = input()
lst = []
d = {}

for i in text:
    lst.append(i)
tup = tuple(lst)

for i in tup:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] = tup.count(i)

for key in sorted(d.keys()):
    print(key+":",d[key],"time/s")
