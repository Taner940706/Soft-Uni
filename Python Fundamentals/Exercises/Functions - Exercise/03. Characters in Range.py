a=input()
b=input()

def between_them():
    for i in range(ord(a)+1,ord(b)):
        print(chr(i), end=" ")
        
between_them()