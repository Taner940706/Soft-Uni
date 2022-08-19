n = int(input())
current = 1
is_current = False
for row in range(1, n+1):
    for col in range(1, row+1):
        if current > n:
            is_current = True
            break
        print(str(current)+' ', end='')
        current += 1
    if is_current:
        break
    print()
