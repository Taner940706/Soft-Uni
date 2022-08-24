a = input().split("-")
t={}
for i in range(10000):
    if a[0].isdigit() == True:
        b=a
        break
    else:
        t[a[0]]=a[1]
    a = input().split("-")

c=int(a[0])
for i in range(c):
    b=input()
    if b not in t.keys():
        print(f"Contact {b} does not exist.")
    else:
        print(b+' '+'->'+' '+t[b])