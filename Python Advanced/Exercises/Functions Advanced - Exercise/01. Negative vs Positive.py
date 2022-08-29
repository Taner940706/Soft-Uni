def pos_neg():
    x = [int(i) for i in input().split(" ")]
    pos = 0
    neg = 0

    for i in x:
        if i < 0:
            neg = neg + i
        else:
            pos = pos + i
    print(neg)
    print(pos)
    if abs(neg) > abs(pos):
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


pos_neg()
