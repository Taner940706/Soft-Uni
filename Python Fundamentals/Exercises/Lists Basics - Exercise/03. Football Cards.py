a=input()
count_a=0
count_b=0
b=a.split(" ")
for i in set(b):
    if i[:1]=="A":
        count_a=count_a+1
    elif i[:1]=="B":
         count_b=count_b+1
    if (11-count_a)<7 or (11-count_b)<7:
       break
print(f"Team A - {11-count_a}; Team B - {11-count_b}")
if (11-count_a)<7 or (11-count_b)<7:
   print("Game was terminated")
    