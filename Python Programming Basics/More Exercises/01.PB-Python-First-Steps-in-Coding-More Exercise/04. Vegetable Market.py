price_fruit=float(input())
price_veg=float(input())
kg_fruit=float(input())
kg_veg=float(input())
res=(price_fruit*kg_fruit+price_veg*kg_veg)/1.94
print(f'{res:.2f}')