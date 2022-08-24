a=input().split(".")
x=[]

for i in a:
    i=int(i)
    x.append(i)


if x[2]<9:
   print(f"{x[0]}.{x[1]}.{(x[2]+1)}")
elif x[2]==9:
     x[2]=0
     if x[1]<9:
        print(f"{x[0]}.{(x[1]+1)}.{x[2]}")
     elif x[1]==9:
          x[1]=0
          print(f"{(x[0]+1)}.{x[1]}.{x[2]}")