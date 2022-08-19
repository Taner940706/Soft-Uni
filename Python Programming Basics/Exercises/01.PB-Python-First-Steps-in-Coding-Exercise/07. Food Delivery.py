count_chicken = int(input())
count_fish = int(input())
count_vegeterian = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegeterian_menu = 8.15
dessert = (chicken_menu*count_chicken + fish_menu*count_fish + vegeterian_menu*count_vegeterian)*0.20

bill = chicken_menu*count_chicken + fish_menu*count_fish + vegeterian_menu*count_vegeterian + dessert + 2.50
print(f"{bill:.2f}")
