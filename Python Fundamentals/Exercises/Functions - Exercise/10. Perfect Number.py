a=int(input())

def isPerfect():
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    if suma==a:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
isPerfect()