n = int(input())


def calc():
    s = ""
    p = ""
    k = ""
    for i in range(10, n+10, 10):
        s = s+"%"
    for m in range(100 , n, -10):
        p = p + "."
    if n < 100:
        print(f"{n}% [{s}{p}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{s}{p}]")


calc()
