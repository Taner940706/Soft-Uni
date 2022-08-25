n=input()

x=n.split(", ")

m=[]

for i in x:
    i=int(i)
    m.append(i)

for s in m:
    if s==0:
        m.remove(s)
        m.append(0)
print(m)