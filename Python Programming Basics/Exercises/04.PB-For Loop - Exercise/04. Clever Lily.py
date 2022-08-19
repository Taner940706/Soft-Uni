age = int(input())
washing_machine = float(input())
toy = int(input())
suma = 0

for i in range(1, age+1):
    if i % 2 == 1:
        suma = suma + toy
    else:
        suma = suma + ((i * 10)/2) - 1


if suma >= washing_machine:
    print(f"Yes! {suma - washing_machine:.2f}")
else:
    print(f"No! {washing_machine-suma:.2f}")