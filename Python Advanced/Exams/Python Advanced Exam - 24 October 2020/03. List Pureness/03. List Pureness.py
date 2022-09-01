from collections import deque
import sys


def best_list_pureness(*avg):

    collection = deque(avg[0])
    rotations = int(avg[1])

    best_pureness = -sys.maxsize
    best_rotation = 0

    for rotation in range(rotations + 1):

        list_pureness = 0
        for idx, val in enumerate(collection):
            list_pureness += idx * val
        if list_pureness > best_pureness:
            best_pureness = list_pureness
            best_rotation = rotation

        el = collection.pop()
        collection.appendleft(el)

    return f"Best pureness {best_pureness} after {best_rotation} rotations"