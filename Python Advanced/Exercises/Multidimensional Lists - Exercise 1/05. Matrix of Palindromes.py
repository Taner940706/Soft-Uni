rows, cols = [int(x) for x in input().split(" ")]

matrix = []


for i in range(rows):
    matrix.append([])
    for j in range(cols):
        matrix[i].append(chr(97+i) + chr((97+i+j)) + chr(97+i))
    s = " ".join(x for x in matrix[i])
    print(s)

