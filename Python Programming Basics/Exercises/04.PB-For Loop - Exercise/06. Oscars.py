name = input()
points_academy = float(input())
jury = int(input())
all_point = 0
for i in range(jury):
    jury_name = input()
    jury_rating = float(input())
    all_point = all_point + (jury_rating*len(jury_name)/2)
    if all_point >= 1250.5 - points_academy:
        print(f"Congratulations, {name} got a nominee for leading role with {all_point + points_academy:.1f}!")
        break

if (all_point + points_academy) < 1250.5:
    print(f"Sorry, {name} you need {1250.5 - all_point - points_academy:.1f} more!")