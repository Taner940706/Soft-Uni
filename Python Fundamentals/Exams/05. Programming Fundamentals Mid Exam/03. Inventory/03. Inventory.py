a = list(input().split(", "))
b = input()


while b != "Craft!":
    c = b.split(" - ")
    if c[0] == "Collect":
        if c[1] not in a:
            a.append(c[1])
    if c[0] == "Drop":
        if c[1] in a:
            a.remove(c[1])
    if c[0] == "Combine Items":
        s = c[1].split(":")
        if s[0] in a:
            a.insert(a.index(s[0])+1, s[1])
    if c[0] == "Renew":
        if c[1] in a:
            a.sort(key=c[1].__eq__)
    b = input()
listToStr = ', '.join([str(elem) for elem in a])
print(listToStr)
