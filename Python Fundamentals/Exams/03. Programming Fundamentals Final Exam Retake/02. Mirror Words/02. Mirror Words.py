import re
txt = input()
pattern_1 = '#{1}[A-z]{3,}\#{2}[A-z]{3,}\#{1}|@{1}[A-z]{3,}\@{2}[A-z]{3,}\@{1}'

t = {}
x = re.findall(pattern_1, txt)

for i in x:
    n = re.sub('[@|#]', "", i)
    if n == n[::-1]:
        y = n[:int((len(n)/2))]
        z = n[int((len(n)/2)):]
        t[y] = z
if len(x) == 0:
    print("No word pairs found!")
else:
    print(f"{len(x)} word pairs found!")
if len(t) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join('{} <=> {}'.format(k, v) for k, v in t.items()))
