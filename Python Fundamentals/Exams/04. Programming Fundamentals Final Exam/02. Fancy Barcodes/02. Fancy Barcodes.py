import re
num = int(input())
pattern_isvalid = '^[@][#]+[A-Z][A-Za-z0-9]{4,}[A-Z][@][#]+$'
s = ""

for i in range(num):
    bar_code = input()
    x = re.findall(pattern_isvalid, bar_code)
    if len(x) == 1:
        k = re.sub('[#|@]', "", x[0])
        t = re.findall('[0-9]', k)
        if len(t) > 0:
            for m in t:
                s = s + m
            print(f"Product group: {s}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
    x = []
    k = []
    t = []
    s = ""
