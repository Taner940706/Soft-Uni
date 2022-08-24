n = int(input())
k = int(input())


def fact():
    pr = 1
    kr = 1
    for i in range(n, 1, -1):
        pr = pr*i
    for s in range(k, 1, -1):
        kr = kr*s
    print(f"{pr/kr:.2f}")


fact()
