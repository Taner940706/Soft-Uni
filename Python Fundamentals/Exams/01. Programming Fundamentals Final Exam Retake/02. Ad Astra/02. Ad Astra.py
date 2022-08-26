import re
txt = input()
pattern = '([#]{1}[a-zA-Z ]+[#]{1}[0-9]{2}\/[0-9]{2}\/[0-9]{2}[#]{1}[0-9]+[#]{1})|([\|]{1}[a-zA-Z ]+[\|]{1}[0-9]{2}\/[0-9]{2}\/[0-9]{2}[\|]{1}[0-9]+[\|]{1})'
suma = 0
x = re.findall(pattern, txt)
t = []
for i in x:
    for k in i:
        if len(k) != 0:
            t.append(k[1:-1])
for i in t:
    m = re.split('[#|\|]', i)
    suma = suma + int(m[2])

print(f"You have food to last you for: {int(suma/2000)} days!")
for i in t:
    m = re.split('[#|\|]', i)
    print(f"Item: {m[0]}, Best before: {m[1]}, Nutrition: {m[2]}")
