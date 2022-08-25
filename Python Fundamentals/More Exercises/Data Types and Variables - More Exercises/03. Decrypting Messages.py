a=int(input())
n=int(input())
c=""
for i in range(n):
    x=input()
    c=c+chr(ord(x)+a)
print(c)