num = int(input())
order = input().split(" ")
stack = []

for i in order:
    i = int(i)
    stack.append(i)
    order[::-1].pop()
    if sum(stack) > num:
        stack.pop()
        order[::-1].append(i)
        break
if len(order) == len(stack):
    order = [int(item) for item in order]
    print(max(order))
    print("Orders complete")
else:
    order = [int(item) for item in order]
    print(max(order))
    list_difference = []
    for item in order:
        if item not in stack:
            list_difference.append(item)
    print(f"Orders left: {' '.join(str(x) for x in list_difference)}")
