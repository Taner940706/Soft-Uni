a=input()
n=int(input())
b=list(a.split(" "))

x=[]

for i in b:
    i=int(i)
    x.append(i)

for k in range(n):
    x.remove(min(x))

str1 = ', '.join(str(e) for e in x)
print(str1)
    