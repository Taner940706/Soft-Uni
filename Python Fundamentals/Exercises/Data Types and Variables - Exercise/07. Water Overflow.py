n=int(input())
suma=0

for i in range(0,n):
    a=int(input())
    if a>255:
        print("Insufficient capacity!")
        pass
    elif a<255:
         suma=suma+a
         if suma>255:
             suma=suma-a
             print("Insufficient capacity!")
             continue
         
print(suma)