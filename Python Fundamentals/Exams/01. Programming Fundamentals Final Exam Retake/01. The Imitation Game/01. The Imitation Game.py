txt = input()
command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        n = int(command[1])
        x = txt[:n]
        txt = txt[n:] + x
    if command[0] == "Insert":
        x = int(command[1])
        txt = txt[:x] + command[2] + txt[x:]
    if command[0] == "ChangeAll":
        x = txt.replace(command[1], command[2])
        txt = x
    command = input()
print(f"The decrypted message is: {txt}")
