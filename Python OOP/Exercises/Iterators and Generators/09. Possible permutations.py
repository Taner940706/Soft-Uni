from itertools import permutations


def possible_permutations(elements):

    result = permutations(elements)

    for perm in result:
        yield list(perm)