n = input().split(" ")
s=""
my_dict={}
for i in n:
    s=s+i
 
for i in s:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

for key, value in my_dict.items():
    print(key+' '+'->'+' '+str(value))