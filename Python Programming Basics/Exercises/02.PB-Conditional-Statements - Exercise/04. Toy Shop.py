price_vacation = float(input())
puzzle_quantity = int(input())
baby_quantity = int(input())
bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

puzzle = 2.60
baby = 3
bear = 4.10
minion = 8.20
truck = 2

all_quantity = puzzle_quantity + baby_quantity + bear_quantity + minion_quantity + truck_quantity
all_bill = puzzle_quantity*puzzle + baby_quantity*baby + bear_quantity*bear + minion_quantity*minion + truck_quantity*truck

if all_quantity >= 50:
    all_bill = 0.75*all_bill

all_bill = all_bill*0.90

if all_bill >= price_vacation:
    print(f"Yes! {all_bill - price_vacation:.2f} lv left.")
else:
    print(f"Not enough money! {price_vacation - all_bill:.2f} lv needed.")