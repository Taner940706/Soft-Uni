import math
num_students = int(input())
lectures = int(input())
add_bonus = int(input())
lec = []
bon = []
total = 0


if lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for i in range(num_students):
        a = int(input())
        total = a / lectures * (5 + add_bonus)
        bon.append(total)
        lec.append(a)
    print(f"Max Bonus: {math.ceil(max(bon))}.")
    k = bon.index(max(bon))
    print(f"The student has attended {lec[k]} lectures.")
