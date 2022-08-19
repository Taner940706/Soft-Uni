dep_sum = float(input())
period = int(input())
rate = float(input())/100
res = dep_sum + (period * ((dep_sum*rate)/12))
print(res)