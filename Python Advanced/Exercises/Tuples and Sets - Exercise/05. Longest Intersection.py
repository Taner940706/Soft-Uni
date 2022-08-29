num = int(input())
set_a = set()
set_b = set()
set_all =[]
vremenen = []


for i in range(num):
    x = input()
    t = x.replace("-", ",")
    t = t.split(",")
    t = [int(i) for i in t]
    for i in range(t[0], t[1]+1):
        set_a.add(i)
    for i in range(t[2], t[3]+1):
        set_b.add(i)
    set_all.append(set_a.intersection(set_b))
    set_a = set()
    set_b = set()
for i in set_all:
    vremenen.append(len(i))
t = max(vremenen)
m = vremenen.index(t)

print(f"Longest intersection is {list(set_all[m])} with length {t}")

    
        
        