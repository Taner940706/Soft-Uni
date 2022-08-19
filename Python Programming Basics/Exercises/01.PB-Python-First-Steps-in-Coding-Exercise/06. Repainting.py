nylon_quantity = int(input())
paint_litre = int(input())
thinner_litre = int(input())
hours = int(input())

nylon_sum = (nylon_quantity+2)*1.50
paint_sum = (paint_litre+paint_litre*0.10)*14.50
thinner_sum = thinner_litre*5.00
extra = 0.40
sum_work = hours*(nylon_sum + paint_sum + thinner_sum + extra)*0.30
res = nylon_sum + paint_sum + thinner_sum + extra + sum_work
print(res)
