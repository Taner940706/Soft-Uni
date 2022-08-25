a=int(input())
b=int(input())
c=int(input())
x=[]
def multiplication():
    count_minus=0
    count_zero=0
    x.append(a)
    x.append(b)
    x.append(c)
    
    for i in x:
        if i<0:
           count_minus=count_minus+1
        elif i==0:
             count_zero=count_zero+1
    if count_zero==0:
       if count_minus%2==0:
          print("positive")
       elif count_minus%2!=0:
            print("negative")
    else:
        print("zero")
multiplication()
    