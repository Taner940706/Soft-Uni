s=input()
b=[]
x=-1
for i in s:
    x=x+1
    if i.isupper()==True:
        b.append(x)
print(b)