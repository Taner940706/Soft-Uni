enter = input()

new_list = ""
explosion = 0
lenght = 0

while lenght < len(enter):
    for i in range(len(enter)):
        if not enter[i] == ">" and explosion > 0:
            explosion -= 1
        elif enter[i] == ">":
            explosion += int(enter[i + 1])
            new_list += enter[i]
        else:
            new_list += enter[i]
        lenght += 1
print(new_list)