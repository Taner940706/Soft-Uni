flower_type = input()
count = int(input())
budget = int(input())
sum = 0
if flower_type == "Roses":
    if count > 80:
        sum = count*5*0.90
    else:
        sum = count*5
elif flower_type == "Dahlias":
    if count > 90:
        sum = count*3.80*0.85
    else:
        sum = count*3.80
elif flower_type == "Tulips":
    if count > 80:
        sum = count*2.80*0.85
    else:
        sum = count*2.80
elif flower_type == "Narcissus":
    if count < 120:
        sum = count*3*1.15
    else:
        sum = count*3
else:
    if count < 80:
       sum = count*2.50*1.20
    else:
        sum = count*2.50
if budget >= sum:
    print(f'Hey, you have a great garden with {count} {flower_type} and {budget-sum:.2f} leva left.')
else:
    print(f'Not enough money, you need {sum-budget:.2f} leva more.')