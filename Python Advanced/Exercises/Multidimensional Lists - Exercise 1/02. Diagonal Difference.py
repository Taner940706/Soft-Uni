rows = int(input())
matrix = []
diagonal = []
reverse_diagonal = []

for _ in range(rows):
    nums = [int(x) for x in input().split(" ")]
    matrix.append(nums)

for i in range(rows):
    diagonal.append(matrix[i][i])
    reverse_diagonal.append(matrix[i][(rows - 1) - i])

print(abs(sum(diagonal) - sum(reverse_diagonal)))
