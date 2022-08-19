import math
a = int(input())
b = int(input())
c = int(input())
total = a + b + c
minutes = total / 60
seconds = total % 60
minutes = math.floor(minutes)
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
