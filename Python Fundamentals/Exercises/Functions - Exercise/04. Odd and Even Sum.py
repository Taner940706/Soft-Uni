a=int(input())

def sums():
    b=str(a)
    sum_odd=0
    sum_even=0
    for i in b:
        i=int(i)
        if i%2==0:
            sum_even=sum_even+i
        elif i%2!=0:
             sum_odd=sum_odd+i
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
sums()