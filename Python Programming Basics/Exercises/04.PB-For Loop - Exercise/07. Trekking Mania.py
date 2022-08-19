groups_climbers = int(input())
group_musalla = 0
group_monblan = 0
group_kilimandjaro = 0
group_k2 = 0
group_everest = 0
all_climbers = 0

for i in range(groups_climbers):
    count_climbers = int(input())
    if count_climbers <= 5:
        group_musalla = group_musalla + count_climbers
    elif 6 <= count_climbers <= 12:
        group_monblan = group_monblan + count_climbers
    elif 13 <= count_climbers <= 25:
        group_kilimandjaro = group_kilimandjaro + count_climbers
    elif 26 <= count_climbers <= 40:
        group_k2 = group_k2 + count_climbers
    else:
        group_everest = group_everest + count_climbers
    all_climbers = all_climbers + count_climbers

print(f"{group_musalla/all_climbers*100:.2f}%")
print(f"{group_monblan/all_climbers*100:.2f}%")
print(f"{group_kilimandjaro/all_climbers*100:.2f}%")
print(f"{group_k2/all_climbers*100:.2f}%")
print(f"{group_everest/all_climbers*100:.2f}%")

