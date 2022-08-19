month = input()
day = int(input())
if day <= 7:
    if month == "May" or month == "October":
        print(f'Apartment: {day*65:.2f} lv.')
        print(f'Studio: {day*50:.2f} lv.')
    elif month == "June" or month == "September":
        print(f'Apartment: {day*65:.2f} lv.')
        print(f'Studio: {day*75.20:.2f} lv.')
    elif month == "July" or month == "August":
        print(f'Apartment: {day*77:.2f} lv.')
        print(f'Studio: {day*76:.2f} lv.')
elif 7 < day <= 14:
    if month == "May" or month == "October":
        print(f'Apartment: {day*65:.2f} lv.')
        print(f'Studio: {day*50*0.95:.2f} lv.')
    elif month == "June" or month == "September":
        print(f'Apartment: {day*68.70:.2f} lv.')
        print(f'Studio: {day*75.20:.2f} lv.')
    elif month == "July" or month == "August":
        print(f'Apartment: {day*77:.2f} lv.')
        print(f'Studio: {day*76:.2f} lv.')
elif day > 14:
    if month == "May" or month == "October":
        print(f'Apartment: {day*65*0.90:.2f} lv.')
        print(f'Studio: {day*50*0.70:.2f} lv.')
    elif month == "June" or month == "September":
        print(f'Apartment: {day*68.70*0.90:.2f} lv.')
        print(f'Studio: {day*75.20*0.80:.2f} lv.')
    elif month == "July" or month == "August":
        print(f'Apartment: {day*77*0.90:.2f} lv.')
        print(f'Studio: {day*76:.2f} lv.')
