def stock_availability(boxes, command, *args):
    t = 0
    if command == "sell":
        if len(args) == 0:
            boxes = boxes[1:]
        else:
            for i in args:
                i = str(i)
                if i.isdigit():
                    i = int(i)
                    boxes = boxes[i:]
                else:
                    t = boxes.count(i)
                    for _ in range(t):
                        if i in boxes:
                            boxes.remove(i)
    elif command == "delivery":
        for i in args:
            boxes.append(i)
    return boxes


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

