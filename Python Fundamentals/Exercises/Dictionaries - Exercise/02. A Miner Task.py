n=input()
t={}
while n != "stop":
    a=int(input())
    if n not in t:
        t[n]=a
    else:
        t[n]=t[n]+a
    n=input()
for key, value in t.items():
    print(key+' '+'->'+' '+str(value))