import math

num = int(input())
suma = 0
set_even = set()
set_odd = set()
k = 1

for i in range(num):
    x = input()
    for i in x:
        suma = suma + ord(i)
    y = suma // k
    if y % 2 == 1:
        set_odd.add(y)
    else:
        set_even.add(y)
    suma = 0
    k += 1

if sum(set_odd) > sum(set_even):
    t = list(set_odd.difference(set_even))
    print(", ".join([str(i) for i in t]))
elif sum(set_odd) < sum(set_even):
    t = list(set_odd.symmetric_difference(set_even))
    print(", ".join([str(i) for i in t]))
elif sum(set_odd) == sum(set_even):
    t = list(set_odd.union(set_even))
    print(", ".join([str(i) for i in t]))
