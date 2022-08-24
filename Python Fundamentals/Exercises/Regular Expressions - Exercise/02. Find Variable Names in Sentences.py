import re
n = input()
s = []
x = re.findall(r"\b_([a-zA-Z0-9]+)\b", n)
print(','.join(x))
