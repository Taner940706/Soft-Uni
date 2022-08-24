str_1 = input()
str_2 = input()
count = 0;
arr = []

for i in str_2:
    count += 1;
    res = str_2[:count] + str_1[count:];
    if res not in arr:
        arr.append(res);
        print(res);