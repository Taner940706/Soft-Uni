a = int(input())
b = int(input())
h = int(input())
v = a*b*h
command = input()
suma = 0
while command != "Done":
    command = int(command)
    suma = suma + command
    if v <= suma:
        print(f"No more free space! You need {suma - v} Cubic meters more.")
        break
    else:
        command = input()
if (v-suma) > 0:
    print(f"{v-suma} Cubic meters left.")