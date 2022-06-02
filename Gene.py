import random

class Gene:
    def __init__(self, id,  weight, value):
        self._id = id
        self._weight = weight
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def ShowTheGene(self):
        print(f'id = {self._id} weight = {self._weight} value = {self._value}')