def next_position(direction, row, col):
    if direction == 'down':
        return row + 1, col
    elif direction == 'up':
        return row -1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1

data = input()

size = int(input())
matrix = []
player_col = 0
player_row = 0

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()

    new_row, new_col = next_position(command, player_row, player_col)
    if new_row < 0 or new_col < 0 or new_row >= size or new_col >= size:
        if data:
            data = data[:-1]
        continue
    matrix[player_row][player_col] = '-'
    player_row, player_col = new_row, new_col

    if matrix[player_row][player_col] != '-':
        data += matrix[player_row][player_col]

    matrix[player_row][player_col] = 'P'

print(data)

for i in range(size):
    print(*matrix[i], sep='')


