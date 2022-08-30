def start_spring(**example_objects):
    springs = {}
    result = ''

    for key, value in example_objects.items():
        if value not in springs.keys():
            springs[value] = ["-"+key]
        else:
            springs[value].append("-"+key)

    d = sorted(springs.items(), key=lambda x: (-len(x[1]), x[0]))
    for tuple_ in d:
        result += tuple_[0]+":" + "\n"
        quantity_list = sorted(tuple_[1])
        result += "\n".join(map(str, quantity_list))
        result += "\n"
    result = result.strip()
    return result