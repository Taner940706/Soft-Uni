a=input()

b=a.split(" ")
x=[]

def check_it(a):
    for i in b:
        i=int(i)
        x.append(i)
    return sorted(x)
m=check_it(a)
print(m)