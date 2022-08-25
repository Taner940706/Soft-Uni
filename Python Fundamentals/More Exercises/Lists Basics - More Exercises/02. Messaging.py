a=input()
b=input()

n=a.split(" ")
suma=0
x=[]

for i in n:
    sum_val = 0
    for digit in str(i):
        sum_val += int(digit)
    x.append(sum_val)

for k in x:
    if len(b)<k:
       k=k-len(b)
       print(b[k], end="")
    else:
        print(b[k], end="")
    b = b[0 : k : ] + b[k + 1 : :]