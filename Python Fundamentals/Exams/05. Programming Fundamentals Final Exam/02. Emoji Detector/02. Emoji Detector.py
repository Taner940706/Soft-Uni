import re
msg = input()
pattern_emoji = '[::|**]{2}[A-Z][a-z]{2,}[::|**]{2}'
pattern_numbers = '[0-9]'
x = re.findall(pattern_emoji, msg)
y = re.findall(pattern_numbers, msg)
pr = 1
suma = 0
real_shady = []
d = {}
for i in x:
    t = i.count("*")
    s = i.count(":")
    if t == 4 or s == 4:
        real_shady.append(i)
for i in y:
    i = int(i)
    pr *= i

for i in real_shady:
    for k in i[2:-2]:
        k = ord(k)
        suma = suma + k
    if i not in d.keys():
        d[i] = suma
    suma = 0
v = {key: val for key, val in d.items() if val > pr}

print(f"Cool threshold: {pr}")
print(f"{len(d.keys())} emojis found in the text. The cool ones are:")
for key in v.keys():
    print(key)
