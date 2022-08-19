hours = int(input())
minutes = int(input()) + 15

if minutes > 59:
    hours += 1
    minutes -= 60
if hours > 23:
    hours = 0

print(f'{hours}:{minutes:02d}')
