
Q = 0.35
P = 0.65
PHEROMONEFORRUN = 1.0
from Meal import *
from Ant import *

class AntAlgorithm:
    def __init__(self, count_ants, count_iteration, max_ant_energy, items, evaporation_coefficient):
        self._count_ants = count_ants
        self._count_iteration = count_iteration
        self._max_ant_energy = max_ant_energy
        self._items = items
        self._evaporation_coefficient = evaporation_coefficient

    @property
    def count_ants(self):
        return self._count_ants

    @count_ants.setter
    def count_ants(self, count_ants):
        self._count_ants = count_ants

    @property
    def count_iteration(self):
        return self._count_iteration

    @count_iteration.setter
    def count_iteration(self, count_iteration):
        self._count_iteration = count_iteration

    @property
    def max_ant_energy(self):
        return self._max_ant_energy

    @max_ant_energy.setter
    def max_ant_energy(self, max_ant_energy):
        self._max_ant_energy = max_ant_energy

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def evaporation_coefficient(self):
        return self._evaporation_coefficient

    @evaporation_coefficient.setter
    def evaporation_coefficient(self, evaporation_coefficient):
        self._evaporation_coefficient = evaporation_coefficient

    def BonAppetit(self):
        menu = []
        i = 0
        while (i < len(self._items[0])):
            menu.append(Meal(self._items[2][i], self._items[0][i], self._items[1][i]))
            i += 1
        i = 0
        best_ant = Ant(self._max_ant_energy)
        while (self._count_iteration > i):
            sum = 0
            j = 0
            while (j < len(menu)):
                sum += (menu[j].pheromone ** P) * ((menu[j].count_food / menu[j].energy) ** Q)
                j += 1
            j = 1
            meal_probability = []
            meal_probability.append((menu[0].pheromone ** P) * ((menu[0].count_food / menu[0].energy) ** Q) / sum)
            while (j < len(menu)):
                meal_probability.append(
                    meal_probability[j - 1] + ((menu[j].pheromone ** P) * (((menu[j].count_food / menu[j].energy) ** Q) / sum)))
                j += 1
            j = 0
            ant_population = []
            while (self._count_ants > j):
                ant_population.append(Ant(self._max_ant_energy).LoadAnt(meal_probability, menu))
                if (best_ant.count_food < ant_population[j].count_food):
                    best_ant = ant_population[j]
                j += 1
            j = 0
            while (self._count_ants > j):
                sum_function = 0
                y = 0
                while (y < len(ant_population[j].order)):
                    sum_function += ant_population[j].order[y].count_food / ant_population[j].order[y].energy
                    y += 1
                y = 0
                pheromone_coefficient = ant_population[j].count_food / best_ant.count_food
                while (y < len(ant_population[j].order)):
                    menu[ant_population[j].order[y].id].pheromone += PHEROMONEFORRUN * pheromone_coefficient / sum_function * (menu[
                        ant_population[j].order[y].id].count_food / menu[ant_population[j].order[y].id].energy)
                    y += 1
                j += 1
            j = 0
            while (j < len(best_ant.order)):
                sum_function += best_ant.order[j].count_food / best_ant.order[j].energy
                j += 1
            j = 0
            while (j < len(best_ant.order)):
                menu[best_ant.order[j].id].pheromone += i * PHEROMONEFORRUN / sum_function * \
                    (menu[best_ant.order[j].id].count_food / menu[best_ant.order[j].id].energy)
                j += 1
            j = 0
            while (len(menu) > j):
                menu[j].pheromone = (1 - self._evaporation_coefficient) * menu[j].pheromone
                j += 1
            print(i)
            i += 1
        best_ant.ShowMeYourOrder()
        result = [best_ant.energy, best_ant.count_food, best_ant.MealsToItems()]
        return result
