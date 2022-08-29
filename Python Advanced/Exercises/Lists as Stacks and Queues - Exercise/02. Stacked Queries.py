num = int(input())
n = []

for i in range(num):
    a = input().split(" ")
    if a[0] == "1":
        n.append(a[1])
    if a[0] == "2":
        if len(n) > 0:
            n.pop()
    if a[0] == "3":
        if len(n) > 0:
            print(max(n))
    if a[0] == "4":
        if len(n) > 0:
            print(min(n))
y = n[::-1]
print(', '.join(y))

