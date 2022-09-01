def flights(*args, **kwargs):
    flight = []
    L2 = []
    new_dict = {}
    for i in args:
        if i == "Finish":
            break
        flight.append(i)

    for i in range(0, len(flight), 2):
        L2.append((flight[i], flight[i + 1]))
    for (key, value) in L2:
        if key in new_dict:
            new_dict[key] += value
        else:
            new_dict[key] = value
    return new_dict