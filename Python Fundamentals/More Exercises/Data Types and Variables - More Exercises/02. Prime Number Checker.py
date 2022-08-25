num = int(input())

flag = True

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag=False
            # break out of loop
            break
        else:
           flag=True
if flag==True:
    print(True)
else:
    print(False)