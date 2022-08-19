n = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if n % num1 == 0 and n % num2 == 0 and n % num3 == 0 and n % num4 == 0:
                    print(f"{num1}{num2}{num3}{num4}", end=" ")
