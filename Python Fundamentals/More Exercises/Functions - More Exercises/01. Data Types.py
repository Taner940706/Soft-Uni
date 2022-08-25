typ=input()
num=input()

def type_of_numa():
    if typ=="int":
        x=int(num)*2
        print(x)
    elif typ=="real":
        x=float(num)*1.5
        print(f"{x:.2f}")
    elif typ=="string":
         print("$"+num+"$")
type_of_numa()