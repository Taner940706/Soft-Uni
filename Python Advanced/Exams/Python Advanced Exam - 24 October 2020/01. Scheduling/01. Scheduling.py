from collections import deque


jobs = deque(int(i) for i in input().split(", "))
ind = int(input())
dict_jobs = {}
clocks = 0

for i in range(len(jobs)):
    if i not in dict_jobs.keys():
        dict_jobs[i] = jobs[i]


sorted_tuples = sorted(dict_jobs.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sorted_tuples}

for key, value in sorted_dict.items():
    if key == ind:
        clocks += value
        break
    else:
        clocks += value

print(clocks)

