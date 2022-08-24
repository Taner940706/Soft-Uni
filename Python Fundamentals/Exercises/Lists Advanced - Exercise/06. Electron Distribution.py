n=int(input())
x=[]
y=[]
suma=0
for i in range(1,n+1):
    i=2*(i**2)
    x.append(i)
for k in x:
    suma=suma+k
    if suma<=n:
        y.append(k)
        
t=sum(y)
y.append(n-t)
print(y)