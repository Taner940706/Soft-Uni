n = int(input())
count = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for i in range(n):
    x = int(input())
    if x < 200:
        count = count + 1
    elif 200 <= x < 400:
        count_1 = count_1 + 1
    elif 400 <= x < 600:
        count_2 = count_2 + 1
    elif 600 <= x < 800:
        count_3 = count_3 + 1
    elif x >= 800:
        count_4 = count_4 + 1

print(f'{count / n * 100:.2f}%')
print(f'{count_1 / n * 100:.2f}%')
print(f'{count_2 / n * 100:.2f}%')
print(f'{count_3 / n * 100:.2f}%')
print(f'{count_4 / n * 100:.2f}%')
