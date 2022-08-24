n=int(input())
x=int(input())

for i in range(x,n-1,-1):
    if i%n==0:
        print(i)
        break