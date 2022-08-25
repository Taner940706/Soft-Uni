n = int(input())
s = ""
p = ""
for i in range(n):
    x = input().split(" ")
    for m in x:
        if "@" in m and "|" in m:
            s = m[m.index("@")+1:m.index("|")]
        if "#" in m and "*" in m:
            p = m[m.index("#")+1:m.index("*")]
    print(f"{s} is {p} years old.")
    s = ""
    p = ""