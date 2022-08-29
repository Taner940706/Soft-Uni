rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

command = input()

while command != "END":
    command = command.split(" ")
    if command[0] == "Add":
        if 0<=int(command[1])<=rows-1 and 0<=int(command[2])<=rows-1:
            matrix[int(command[1])][int(command[2])] = matrix[int(command[1])][int(command[2])] + int(command[3])
        else:
            print("Invalid coordinates")
    if command[0] == "Subtract":
        if 0<=int(command[1])<=rows and 0<=int(command[2])<=rows:
            matrix[int(command[1])][int(command[2])] = matrix[int(command[1])][int(command[2])] - int(command[3])
        else:
            print("Invalid coordinates")
    command = input()
for i in range(rows):
    s = " ".join(str(x) for x in matrix[i])
    print(s)