import numpy as np

class BruteForceMethod:
    def __init__ (self, items, maxWeight):
        self._items = items
        self._maxWeight = maxWeight


    def Iteration(self, result, itemIndex):
        if ((self._items[0][itemIndex] == self._maxWeight)|(itemIndex > len(self._items))):

            return None
        # if (self._items[0][itemIndex] < self._maxWeight - weight):
            # value += self._items[1][itemIndex]
            # weight += self._items[0][itemIndex]
            # itemIndex += 1


    def ToInfinityAndBeyond(self):
        result = [0, 0, 0, 0]
        # result[0] = weight if item taken, result[1] = value if item taken
        # result[2] = weight if item taken, result[3] = value if item taken
        result = self.Iteration(self, result, 0, )
        return np.max(result[1], result[3])