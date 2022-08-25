import math
n1=float(input())
n2=float(input())
m1=float(input())
m2=float(input())
a1=float(input())
a2=float(input())
b1=float(input())
b2=float(input())

def closeTo():
    if math.sqrt((n1-n2)**2+(m1-m2)**2)>math.sqrt((a1-a2)**2+(b1-b2)**2):
       if n1**2+n2**2>m1**2+m2**2:
          print(f"({math.floor(m1)}, {math.floor(m2)})({math.floor(n1)}, {math.floor(n2)})")
       elif n1**2+n2**2<m1**2+m2**2:
            print(f"({math.floor(n1)}, {math.floor(n2)})({math.floor(m1)}, {math.floor(m2)})")
       elif n1**2+n2**2==m1**2+m2**2:
            print(f"({math.floor(n1)}, {math.floor(n2)})({math.floor(m1)}, {math.floor(m2)})")
    elif math.sqrt((n1-n2)**2+(m1-m2)**2)<math.sqrt((a1-a2)**2+(b1-b2)**2):
         if a1**2+a2**2>b1**2+b2**2:
            print(f"({math.floor(b1)}, {math.floor(b2)})({math.floor(a1)}, {math.floor(a2)})")
         elif a1**2+a2**2<b1**2+b2**2:
              print(f"({math.floor(a1)}, {math.floor(a2)})({math.floor(b1)}, {math.floor(b2)})")
         elif a1**2+a2**2==b1**2+b2**2:
              print(f"({math.floor(a1)}, {math.floor(a2)})({math.floor(b1)}, {math.floor(b2)})")
    elif math.sqrt((n1-n2)**2+(m1-m2)**2)==math.sqrt((a1-a2)**2+(b1-b2)**2):
         if n1**2+n2**2>m1**2+m2**2:
            print(f"({math.floor(m1)}, {math.floor(m2)})({math.floor(n1)}, {math.floor(n2)})")
         elif n1**2+n2**2<m1**2+m2**2:
              print(f"({math.floor(n1)}, {math.floor(n2)})({math.floor(m1)}, {math.floor(m2)})")
         elif n1**2+n2**2==m1**2+m2**2:
              print(f"({math.floor(n1)}, {math.floor(n2)})({math.floor(m1)}, {math.floor(m2)})")
closeTo()