import math
n1=float(input())
n2=float(input())
m1=float(input())
m2=float(input())

def closeTo():
    if n1**2+n2**2>m1**2+m2**2:
       print(f"({math.floor(m1)}, {math.floor(m2)})")
    elif n1**2+n2**2<m1**2+m2**2:
         print(f"({math.floor(n1)}, {math.floor(n2)})")
    elif n1**2+n2**2==m1**2+m2**2:
         print(f"({math.floor(n1)}, {math.floor(n2)})")
closeTo()