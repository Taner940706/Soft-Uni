import math
count_tournament = int(input())
initial_points = int(input())
all_points = 0
count_w = 0
for i in range(count_tournament):
    tournament_reach = input()
    if tournament_reach == "W":
        all_points = all_points + 2000
        count_w = count_w + 1
    elif tournament_reach == "F":
        all_points = all_points + 1200
    elif tournament_reach == "SF":
        all_points = all_points + 720
print(f"Final points: {all_points + initial_points}")
print(f"Average points: {math.floor(all_points/count_tournament)}")
print(f"{count_w/count_tournament*100:.2f}%")
