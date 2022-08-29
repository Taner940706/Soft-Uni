n = int(input());
arr = [];
flag = 0;

for i in range(n):
    x = int(input())
    arr.append(x)

for ind in range(len(arr)):
    if arr[ind] == sum(arr[:ind]+arr[ind+1:]):
        print("Yes");
        print(f"Sum = {arr[ind]}")
        flag = 1;
        break;
if flag == 0:
    arr.sort();
    print("No")
    print(f"Diff = {abs(arr[-1] - sum(arr[:-1]))}")
        
        