n = int(input())
salary = int(input())
for i in range(n):
    x = input()
    if x == "Facebook":
        salary = salary - 150
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif x == "Instagram":
        salary = salary-100
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif x == "Reddit":
        salary = salary - 50
        if salary <= 0:
            print("You have lost your salary.")
            break
if salary > 0:
    print(salary)
