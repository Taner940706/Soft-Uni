a=input()
b=[]

for i in a:
    b.append(int(i))


x=[]
x=sorted(b, reverse=True)

s=""
for m in x:
    s=s+str(m)
    
print(s)
