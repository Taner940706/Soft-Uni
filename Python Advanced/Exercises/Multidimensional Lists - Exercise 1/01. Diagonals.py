rows = int(input())
matrix = []
diagonal = []
reverse_diagonal = []

for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)

for i in range(rows):
    diagonal.append(matrix[i][i])
    reverse_diagonal.append(matrix[i][(rows - 1) - i])

print(f"Primary diagonal: {', '.join([str(i) for i in diagonal])}. Sum: {sum(diagonal)}")
print(f"Secondary diagonal: {', '.join([str(i) for i in reverse_diagonal])}. Sum: {sum(reverse_diagonal)}")
