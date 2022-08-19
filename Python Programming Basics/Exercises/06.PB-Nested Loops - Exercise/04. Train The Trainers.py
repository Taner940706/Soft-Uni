n = int(input())
x = input()
suma = 0
res = 0
final = 0
y = 0
while x != "Finish":
    for i in range(n):
        t = float(input())
        suma = suma + t
    rez = suma / n
    print(f"{x} - {res:.2f}.")
    final = final + res
    suma = 0
    y = y + 1
    x = input()
print(f"Student's final assessment is {final / y:.2f}.")
