a = input().split(" ")
x = []
comm = input()
for m in a:
    m = int(m)
    x.append(m)

while comm != "end":
    comm_1 = comm.split(" ")
    if comm_1[0] == "swap":
        comm_1[1] = int(comm_1[1])
        comm_1[2] = int(comm_1[2])
        x[comm_1[1]], x[comm_1[2]] = x[comm_1[2]], x[comm_1[1]]
    elif comm_1[0] == "multiply":
        comm_1[1] = int(comm_1[1])
        comm_1[2] = int(comm_1[2])
        x[comm_1[1]] = x[comm_1[1]]*x[comm_1[2]]
    elif comm_1[0] == "decrease":
        for i in range(len(x)):
            x[i] -= 1
    comm = input()
listToStr = ', '.join([str(elem) for elem in x])
print(listToStr)
