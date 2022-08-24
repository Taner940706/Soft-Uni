n = int(input())

for i in range(n):
    word = input()
    if "." in word or "_" in word or "," in word:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")