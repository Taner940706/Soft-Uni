a = int(input())
b = int(input())
oper = input()
if oper == "+":
    if (a+b) % 2 == 0:
        print(f'{a} + {b} = {a+b} - even')
    else:
        print(f'{a} + {b} = {a+b} - odd')
elif oper == "-":
    if (a-b) % 2 == 0:
        print(f'{a} - {b} = {a-b} - even')
    else:
        print(f'{a} - {b} = {a-b} - odd')
elif oper == "*":
    if (a*b) % 2 == 0:
        print(f'{a} * {b} = {a*b} - even')
    else:
        print(f'{a} * {b} = {a*b} - odd')
elif oper == "/":
    if b != 0:
        if (a/b) % 2 == 0:
            print(f'{a} / {b} = {a/b:.2f}')
        else:
            print(f'{a} / {b} = {a/b:.2f}')
    else:
        print(f'Cannot divide {a} by zero')
elif oper == "%":
    if b != 0:
        if (a % b) % 2 == 0:
            print(f'{a} % {b} = {a%b}')
        else:
            print(f'{a} % {b} = {a%b}')
    else:
        print(f'Cannot divide {a} by zero')
