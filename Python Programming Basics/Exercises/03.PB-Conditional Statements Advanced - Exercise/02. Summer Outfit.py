temp = int(input())
day = input()
if 10 <= temp <= 18:
    if day == "Morning":
        print(f"It's {temp} degrees, get your Sweatshirt and Sneakers.")
    elif day == "Afternoon":
        print(f"It's {temp} degrees, get your Shirt and Moccasins.")
    else:
        print(f"It's {temp} degrees, get your Shirt and Moccasins.")
elif 18 < temp <= 24:
    if day == "Morning":
        print(f"It's {temp} degrees, get your Shirt and Moccasins.")
    elif day == "Afternoon":
        print(f"It's {temp} degrees, get your T-Shirt and Sandals.")
    else:
        print(f"It's {temp} degrees, get your Shirt and Moccasins.")
elif temp >= 25:
    if day == "Morning":
        print(f"It's {temp} degrees, get your T-Shirt and Sandals.")
    elif day == "Afternoon":
        print(f"It's {temp} degrees, get your Swim Suit and Barefoot.")
    else:
        print(f"It's {temp} degrees, get your Shirt and Moccasins.")
