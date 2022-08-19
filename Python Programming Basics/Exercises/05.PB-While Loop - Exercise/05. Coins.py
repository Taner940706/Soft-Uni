import math
coins = float(input())
br = 0
coins = 100*coins
while coins > 0:
    if coins >= 200:
        coins = coins - 200
        br = br + 1
    elif 200 > coins >= 100:
        coins = coins - 100
        br = br + 1
    elif 100 > coins >= 50:
        coins = coins - 50
        br = br + 1
    elif 50 > coins >= 20:
        coins = coins - 20
        br = br + 1
    elif 20 > coins >= 10:
        coins = coins - 10
        br = br + 1
    elif 10 > coins >= 5:
        coins = coins - 5
        br = br + 1
    elif 5 > coins >= 2:
        coins = coins - 2
        br = br + 1
    elif coins == 1:
        coins = coins - 1
        br = br + 1
    coins = math.floor(coins)
print(br)
