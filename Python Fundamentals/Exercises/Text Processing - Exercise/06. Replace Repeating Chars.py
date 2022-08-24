n = input()
s = ""
for i in n:
    if len(s) < 1:
        s = s + i
    elif len(s) >= 1:
        s = s + i
        if s[-1] == s[-2]:
            s = s[:-1]
print(s)
