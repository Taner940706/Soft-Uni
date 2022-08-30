size = 6
matrix = []
for r in range(size):
    matrix.append(input().split())
result = 0
for _ in range(3):
    row, col = [int(i) for i in input().strip('()').split(', ')]
    if row < 0 or col < 0 or row >= size or col >= size:
        continue
    if matrix[row][col] == 'B':
        for i in range(len(matrix)):
            if matrix[i][col].isdigit():
                result += int(matrix[i][col])
        matrix[row][col] = '.'

if 100 <= result <= 199:
    print(f"Good job! You scored {result} points, and you've won Football.")
elif 200 <= result <= 299:
    print(f"Good job! You scored {result} points, and you've won Teddy Bear.")
elif result >= 300:
    print(f"Good job! You scored {result} points, and you've won Lego Construction Set.")
else:
    print(f'Sorry! You need {100 - result} points more to win a prize.')