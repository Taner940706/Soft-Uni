import re
n = input().split(", ")


for i in n:
    if (len(i) >= 3) and (len(i) <= 16):
        if re.match("^[A-Za-z0-9_-]*$", i):
            print(i)
