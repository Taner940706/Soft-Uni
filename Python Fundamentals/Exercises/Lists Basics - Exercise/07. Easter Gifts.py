gifts = input().split(" ")
command = input()
while command != "No Money":
    comm = command.split(" ");
    if comm[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == comm[1]:
                gifts[i] = "None"
    elif comm[0] == "Required":
        if int(comm[2]) <= len(gifts) - 1:
            gifts[int(comm[2])] = comm[1];
    elif comm[0] == "JustInCase":
        gifts[-1] = comm[1];
    command = input();

x = [i for i in gifts if i != "None"]
print(" ".join(x))
            