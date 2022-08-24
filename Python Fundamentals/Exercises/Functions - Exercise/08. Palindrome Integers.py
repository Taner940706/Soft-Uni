a=input()
b=a.split(", ")

x=[]

for i in b:
    x.append(i)

def isPalindrome():
    for s in x:
        if s[::]==s[::-1]:
            print(True)
        else:
            print(False)
isPalindrome()