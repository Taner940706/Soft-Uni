client_type = input()
row = int(input())
column = int(input())

if client_type == "Premiere":
    print(f"{row*column*12:.2f} leva")
elif client_type == "Normal":
    print(f"{row * column * 7.50:.2f} leva")
else:
    print(f"{row * column * 5:.2f} leva")
