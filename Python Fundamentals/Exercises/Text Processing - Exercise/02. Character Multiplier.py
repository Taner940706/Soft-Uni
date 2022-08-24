n = input().split(" ")
suma = 0
a = n[0]
b = n[1]
mul = 1
a = [ord(i) for i in a]
b = [ord(i) for i in b]


if len(a) < len(b):
    x = len(b) - len(a)
    for i in range(x):
        a.append(int(1))
elif len(a) > len(b):
     x = len(a) - len(b)
     for i in range(x):
         b.append(int(1))

for i in range(len(a)):
    mul=a[i]*b[i]
    suma = suma + mul
print(suma)
        