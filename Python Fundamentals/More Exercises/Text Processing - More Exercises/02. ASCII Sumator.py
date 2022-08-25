a = input()
b = input()
c = input()
c = [ord(i) for i in c]
s = []
suma = 0
for i in range(ord(a)+1, ord(b), 1):
    s.append(i)
for i in c:
    if i in s:
        suma = suma + i

print(suma)
