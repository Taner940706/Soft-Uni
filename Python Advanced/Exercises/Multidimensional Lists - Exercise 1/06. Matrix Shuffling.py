rows, cols = [int(x) for x in input().split(" ")]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split(" ")])

command = input()

while command != "END":
    command = command.split(" ")
    if command[0] == "swap" and len(command) == 5:
        if 0<=int(command[1])<=rows and 0<=int(command[3])<=rows and 0<=int(command[2])<=cols and 0<=int(command[4])<=cols:
            tmp = matrix[int(command[1])][int(command[2])]
            matrix[int(command[1])][int(command[2])] = matrix[int(command[3])][int(command[4])]
            matrix[int(command[3])][int(command[4])] = tmp
            for i in range(rows):
                s = " ".join(x for x in matrix[i])
                print(s)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()