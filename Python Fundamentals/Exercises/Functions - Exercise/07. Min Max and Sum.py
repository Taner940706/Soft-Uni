a=input()

b=a.split(" ")
x=[]

def check_it():
    for i in b:
        i=int(i)
        x.append(i)
    print(f"The minimum number is {min(x)}")
    print(f"The maximum number is {max(x)}")
    print(f"The sum number is: {sum(x)}")
check_it()