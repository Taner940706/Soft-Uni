def tribonacchi(n):
    if n == 0:
        res = [0]
    elif n == 1:
        res = [1]
    elif n == 2:
        res = [1,1]
    else:
        res = [1,1];
        for _ in range(n-2):
            x = sum(res[-3:]);
            res.append(x)
    print(" ".join([str(x) for x in res]))
        
n = int(input())
tribonacchi(n)    
 