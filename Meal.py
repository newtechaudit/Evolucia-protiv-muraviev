import random

class Investment:
    def __init__(self, id, energy, count_food):
        self._id = id
        self._energy = energy
        self._count_food = count_food
        self._pheromone = 1.0


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, energy):
        self._energy = energy

    @property
    def count_food(self):
        return self._count_food

    @count_food.setter
    def count_food(self, count_food):
        self._count_food = count_food

    @property
    def pheromone(self):
        return self._pheromone

    @pheromone.setter
    def pheromone(self, pheromone):
        self._pheromone = pheromone

    def ShowTheDish(self):
        print(f'id = {self._id} weight = {self._energy} value = {self._count_food}')
