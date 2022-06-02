import random

class Ant:
    def __init__(self, max_energy):
        self._max_energy = max_energy
        self._energy = 0
        self._count_food = 0
        self._order = []

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, energy):
        self._energy = energy

    @property
    def max_energy(self):
        return self._max_energy

    @max_energy.setter
    def max_energy(self, max_energy):
        self._max_energy = max_energy

    @property
    def count_food(self):
        return self._count_food

    @count_food.setter
    def count_food(self, count_food):
        self._count_food = count_food

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, order):
        self._order = order

    # @property
    # def count_pheromone(self):
    #     return self._count_pheromone
    #
    # @count_pheromone.setter
    # def count_pheromone(self, count_pheromone):
    #     self._count_pheromone = count_pheromone

    def MealsToItems(self):
        i = 0
        items = []
        while (len(self._order) > i):
            items.append(self._order[i].id)
            i += 1
        return items

    def ShowMeYourOrder(self):
        order_id = '[ '
        i = 0
        while (len(self._order) > i):
            order_id = order_id + str(self._order[i].id) + ' '
            i += 1
        order_id = order_id + ']'
        print(f'weight = {self._energy} value = {self._count_food} {order_id}')

    def LoadAnt(self, meal_probability, menu):
        min_energy_meal = menu[0].energy
        min_energy_iter = 0
        meal_availability = [1] * len(menu)
        while ((self._max_energy - self._energy) >= min_energy_meal):
            rand = random.random()
            k = 0
            while (k < (len(menu))):
                if ((meal_probability[k] >= rand) & ((meal_availability[k] == 0) | ((self._max_energy - self._energy) < menu[k].energy))):
                    break
                if ((meal_probability[k] >= rand) & (meal_availability[k] == 1) & ((self._max_energy - self._energy) >= menu[k].energy)):
                    meal_availability[k] = 0
                    self._order.append(menu[k])
                    self._energy += menu[k].energy
                    self._count_food += menu[k].count_food
                    if (k == min_energy_iter):
                        meal_availability[min_energy_iter] = 0
                        min_energy_iter = next((j for j, x in enumerate(meal_availability) if x), None)
                        if (min_energy_iter != None):
                            min_energy_meal = menu[min_energy_iter].energy
                        else:
                            break
                    break
                k += 1
        return self
