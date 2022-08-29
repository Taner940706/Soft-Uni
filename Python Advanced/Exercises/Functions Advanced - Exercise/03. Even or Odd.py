def even_odd(*args):
    command = args[-1]
    nums = args[:-1]
    even_nums = []
    odd_nums = []

    for i in nums:
        i = int(i)
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    if command == "even":
        return even_nums
    else:
        return odd_nums