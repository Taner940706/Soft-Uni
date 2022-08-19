budget = float(input())
season = input()
if budget <= 100:
    if season == "summer":
        print("Somewhere in Bulgaria")
        print(f'Camp - {budget*0.30:.2f}')
    else:
        print("Somewhere in Bulgaria")
        print(f'Hotel - {budget*0.70:.2f}')
elif budget > 100 and budget <= 1000:
    if season == "summer":
        print("Somewhere in Balkans")
        print(f'Camp - {budget*0.40:.2f}')
    else:
        print("Somewhere in Balkans")
        print(f'Hotel - {budget*0.80:.2f}')
else:
    print("Somewhere in Europe")
    print(f'Hotel - {budget*0.90:.2f}')