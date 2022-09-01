from collections import deque as dq

males = [int(i) for i in input().split()]
females = dq(int(i) for i in input().split())
count = 0
while males and females:
    female = females[0]
    male = males[-1]

    if female <= 0 or male <= 0:
        if female <= 0:
            females.popleft()
        if male <= 0:
            males.pop()
        continue
    if female % 25 == 0 or male % 25 == 0:
        if female % 25 == 0:
            females.popleft()
            if females:
                females.popleft()
        if male % 25 == 0:
            males.pop()
            if males:
                males.pop()
        continue

    if female == male:
        females.popleft()
        males.pop()
        count += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {count}")
if males:
    print(f"Males left: {', '.join(str(i) for i in reversed(males))}")
else:
    print('Males left: none')

if females:
    print(f"Females left: {', '.join(str(i) for i in females)}")
else:
    print('Females left: none')
