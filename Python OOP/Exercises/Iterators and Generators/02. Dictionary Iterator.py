from collections import deque


class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = deque(self.dictionary.keys())
        self.keys_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.keys) == 0:
            raise StopIteration
        key = self.keys.popleft()
        value = self.dictionary[key]
        self.keys_idx += 1
        return key, value