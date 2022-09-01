from collections import deque

orders = deque(int(i) for i in input().split(", "))
employees = [int(i) for i in input().split(", ")]
pizza = 0


while employees and orders:

    employee = employees[-1]
    order = orders[0]

    if order >= 11 or order <= 0:
        orders.popleft()
        continue

    if order > employee:
        x = order - employee
        pizza += employee
        orders.popleft()
        employees.pop()
        orders.appendleft(x)

    if order <= employee:
        orders.popleft()
        employees.pop()
        pizza += order


if len(orders) == 0:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza}")
    print(f"Employees: {', '.join([str(i) for i in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(i) for i in orders])}")