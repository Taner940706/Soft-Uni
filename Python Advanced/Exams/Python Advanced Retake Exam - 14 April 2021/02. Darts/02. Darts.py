def calculate_scored_points(m, i, j):
    scored_points = 0
    if m[i][j].isdigit():
        scored_points = int(m[i][j])
    elif m[i][j] == 'D':
        scored_points = (int(m[i][0]) + int(m[i][-1]) + int(m[0][j]) + int(m[-1][j])) * 2
    elif m[i][j] == 'T':
        scored_points = (int(m[i][0]) + int(m[i][-1]) + int(m[0][j]) + int(m[-1][j])) * 3
    elif m[i][j] == 'B':
        return scored_points
    return scored_points


first_player, second_player = input().split(', ')
matrix = [[char for char in input().split()] for row in range(7)]

first_player_score = 501
second_player_score = 501

first_player_turns = 0
second_player_turns = 0

turns = 1

while True:
    coordinates = eval(input())
    row = coordinates[0]
    col = coordinates[1]

    if row in range(len(matrix)) and col in range(len(matrix)):
        if turns % 2 != 0:
            first_player_turns += 1
            result = calculate_scored_points(matrix, row, col)
            if result == 0:
                first_player_score = 0
                break
            else:
                first_player_score -= result
        else:
            second_player_turns += 1
            result = calculate_scored_points(matrix, row, col)
            if result == 0:
                second_player_score = 0
                break
            else:
                second_player_score -= result
    else:  # HERE
        if turns % 2 != 0:
            first_player_turns += 1
        else:
            second_player_turns += 1

    turns += 1

    if first_player_score <= 0 or second_player_score <= 0:
        break

if first_player_score <= 0:
    print(f'{first_player} won the game with {first_player_turns} throws!')
else:
    print(f'{second_player} won the game with {second_player_turns} throws!')