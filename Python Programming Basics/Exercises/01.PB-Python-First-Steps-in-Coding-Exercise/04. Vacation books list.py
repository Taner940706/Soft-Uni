import math
all_pages = int(input())
pages_per_hour = int(input())
days = int(input())

res = all_pages/(days*pages_per_hour)
print(math.floor(res))
