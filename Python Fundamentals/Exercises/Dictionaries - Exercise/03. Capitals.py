a=input().split(", ")
b=input().split(", ")

x=dict(zip(a,b))
for key, value in x.items():
    print(key+' '+'->'+' '+str(value))