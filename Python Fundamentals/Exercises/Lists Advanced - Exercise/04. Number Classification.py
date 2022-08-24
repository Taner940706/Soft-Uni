a=input().split(", ")
m=[]
n_pos=[]
n_neg=[]
n_even=[]
n_odd=[]
for i in a:
    i=int(i)
    m.append(i)

x_pos=[i for i in m if i>=0]
x_neg=[i for i in m if i<0]
x_odd=[i for i in m if i%2!=0]
x_even=[i for i in m if i%2==0]

for i in x_pos:
    i=str(i)
    n_pos.append(i)

y_pos=", ".join(n_pos)
print(f"Positive: {y_pos}")

for i in x_neg:
    i=str(i)
    n_neg.append(i)

y_neg=", ".join(n_neg)
print(f"Negative: {y_neg}")

for i in x_even:
    i=str(i)
    n_even.append(i)

y_even=", ".join(n_even)
print(f"Even: {y_even}")

for i in x_odd:
    i=str(i)
    n_odd.append(i)

y_odd=", ".join(n_odd)
print(f"Odd: {y_odd}")
