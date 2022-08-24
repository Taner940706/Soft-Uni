n = int(input())
free_chairs = 0

for i in range(1, n + 1):
    input_chairs = input().split(' ')
    chairs = int(len(input_chairs[0]))
    needed = int(input_chairs[1])

    if chairs < needed:
        print(f'{needed - chairs} more chairs needed in room {i}')
        free_chairs -= needed - chairs
    elif chairs > needed:
        free_chairs += chairs - needed

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')