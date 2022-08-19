days = int(input())
type_room = input()
rating = input()
cost = 0

if days < 10:
    if type_room == "room for one person":
        cost = (days - 1) * 18
    elif type_room == "apartment":
        cost = ((days - 1) * 25) * 0.7
    else:
        cost = ((days - 1) * 35) * 0.9
elif 10 <= days < 15:
    if type_room == "room for one person":
        cost = (days - 1) * 18
    elif type_room == "apartment":
        cost = ((days - 1) * 25) * 0.65
    else:
        cost = ((days - 1) * 35) * 0.85
elif days >= 15:
    if type_room == "room for one person":
        cost = (days - 1) * 18
    elif type_room == "apartment":
        cost = ((days - 1) * 25) * 0.50
    else:
        cost = ((days - 1) * 35) * 0.80
if rating == "positive":
    cost = cost * 1.25
else:
    cost = cost * 0.90
print(f"{cost:.2f}")
