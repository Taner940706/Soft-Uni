n = input().split(" ")
x = []
y = []
br = 0
for i in n:
    i = int(i)
    x.append(i)


avg = sum(x)/len(x)
for i in x:
    if i > avg:
        y.append(i)
k = sorted(y, reverse=True)

if max(x) == avg:
    print("No")
else:
    listToStr = ' '.join([str(elem) for elem in k[:5]])
    print(listToStr)


