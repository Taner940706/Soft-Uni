import math


class sequence_repeat:

    def __init__(self, sequence, number):
        self.number = number
        self.sequence = sequence
        self.start = 0
        self.x = ""

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.number - 1:
            t = math.floor(self.start / len(self.sequence)) + 1
            self.sequence = t * self.sequence
            self.x = self.sequence[self.start]
            self.start += 1
            return self.x
        else:
            raise StopIteration()