nums = input().split(" ")
set_a = set()
set_b = set()

for i in range(int(nums[0])):
    x = input()
    set_a.add(x)
for i in range(int(nums[1])):
    x = input()
    set_b.add(x)
n = set_a.intersection(set_b)
for i in n:
    print(i)