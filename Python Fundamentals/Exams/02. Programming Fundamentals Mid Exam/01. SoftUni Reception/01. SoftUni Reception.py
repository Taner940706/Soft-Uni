a = int(input())
b = int(input())
c = int(input())
d = int(input())
br = 0

per_hour = a + b + c

for i in range(0, d, per_hour):
    br = br + 1
    if br % 4 == 0:
        br = br + 1
print(f"Time needed: {br}h.")

