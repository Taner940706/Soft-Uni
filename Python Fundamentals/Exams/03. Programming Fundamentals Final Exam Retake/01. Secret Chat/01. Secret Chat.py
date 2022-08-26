txt = input()
command = input()

while command != "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        k = int(command[1])
        txt = txt[:k] + " " + txt[k:]
        print(txt)
    if command[0] == "Reverse":
        if command[1] in txt:
            x = command[1]
            y = txt.replace(x, "", 1)
            x = x[::-1]
            txt = y + x
            print(txt)
        else:
            print("error")
    if command[0] == "ChangeAll":
        x = command[1]
        y = command[2]
        z = txt.replace(x, y)
        txt = z
        print(txt)
    command = input()
print(f"You have a new text message: {txt}")
