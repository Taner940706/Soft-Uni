num = int(input())
nums = set()

for i in range(num):
    x = input().split(" ")
    for n in x:
        nums.add(n)
for i in nums:
    print(i)
