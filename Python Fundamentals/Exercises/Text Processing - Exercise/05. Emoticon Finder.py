n = input()

for i in range(len(n)):
    if n[i] == ":" and n[i+1].isdigit() == False:
        print(f"{n[i]}{n[i+1]}")
