contests = {}

while True:
    line1 = input()
    if line1 == "end of contests":
        break

    contest, password = line1.split(":")
    contests[contest] = password

ratings = {}

while True:
    line2 = input()
    if line2 == "end of submissions":
        break

    tokens = line2.split("=>")
    contest = tokens[0]
    password = tokens[1]
    username = tokens[2]
    points = int(tokens[3])

    if contest in contests and contests[contest] == password:
        if username not in ratings:
            ratings[username] = {contest: points}
        else:
            if contest in ratings[username]:
                if ratings[username][contest] < points:
                    ratings[username][contest] = points
            else:
                ratings[username][contest] = points

ordered_ratings = {n: v for n, v in (sorted(ratings.items()))}
for key, value in ordered_ratings.items():
    v = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    ordered_ratings[key] = v

max_points = 0
best_candidate = ''

for key, value in ordered_ratings.items():
    current_points = 0
    for sk, sv in value.items():
        current_points += sv
    if current_points > max_points:
        max_points = current_points
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for key, value in ordered_ratings.items():
    print(key)
    for c, p in value.items():
        print(f"#  {c} -> {p}")
