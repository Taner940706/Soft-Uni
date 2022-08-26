code = input()
command = input()

while command != "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        if command[1] in code:
            print(f"{code} contains {command[1]}")
        if command[1] not in code:
            print("Substring not found!")
    if command[0] == "Flip":
        if command[1] == "Upper":
            a = int(command[2])
            b = int(command[3])
            code = code[:a] + code[a:b].upper() + code[b:]
            print(code)
        if command[1] == "Lower":
            a = int(command[2])
            b = int(command[3])
            code = code[:a] + code[a:b].lower() + code[b:]
            print(code)
    if command[0] == "Slice":
        a = int(command[1])
        b = int(command[2])
        code = code[:a] + code[b:]
        print(code)
    command = input()
print(f"Your activation key is: {code}")

