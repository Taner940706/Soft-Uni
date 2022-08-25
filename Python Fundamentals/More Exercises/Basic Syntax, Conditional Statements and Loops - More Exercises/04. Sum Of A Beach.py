s=input()
a=["Water","Sun", "Fish", "Sand"]
s=s.lower()
count1=0
for i in a:
    if i.lower() in s:
        count1=count1+s.count(i.lower())
print(count1)