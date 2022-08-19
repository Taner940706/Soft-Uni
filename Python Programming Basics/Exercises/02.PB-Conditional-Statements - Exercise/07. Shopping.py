budget = float(input())
videocard_quantity = int(input())
processor_quantity = int(input())
ram_quantity = int(input())
bill = 0
videocard_price = 250
processor_price = 0.35*(videocard_price*videocard_quantity)
ram = 0.10*(videocard_price*videocard_quantity)

if videocard_quantity > processor_quantity:
    bill = (videocard_price*videocard_quantity + processor_price*processor_quantity + ram*ram_quantity)*0.85
else:
    bill = videocard_price*videocard_quantity + processor_price*processor_quantity + ram*ram_quantity
if budget >= bill:
    print(f"You have {budget - bill:.2f} leva left!")
else:
    print(f"Not enough money! You need {bill - budget:.2f} leva more!")
