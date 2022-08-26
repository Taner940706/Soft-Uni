password = input()
command = input()
new_password = ""
while command != "Done":
    command = command.split(" ")
    if command[0] == "TakeOdd":
        for i in range(len(password)):
            if i % 2 == 1:
                new_password = new_password + password[i]
        password = new_password
        new_password = ""
        print(password)
    if command[0] == "Cut":
        a = int(command[1])
        b = int(command[2])
        password = password[:a] + password[(a+b):]
        print(password)
    if command[0] == "Substitute":
        if command[1] in password:
            x = password.replace(command[1], command[2])
            password = x
            print(password)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {password}")
