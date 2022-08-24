n=int(input())
res=0
s=""
x=[]
y=[]
for i in range(n):
    weight=int(input())
    time=int(input())
    quality=int(input())
    res=(weight/time)**quality
    s=f"{weight} : {time} = {int(res)} ({quality})"
    y.append(res)
    x.append(s)
    res=0
    s=""
k=max(y)
ind=y.index(k)
print(x[ind])