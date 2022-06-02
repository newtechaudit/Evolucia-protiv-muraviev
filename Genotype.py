from Gene import *


def TransformationGenes(items):
    i = 0
    genes = []
    while (len(items[0]) > i):
        genes.append(Gene(items[2][i], items[0][i], items[1][i]))
        i += 1
    return genes

class Genotype:
    def __init__(self, maxWeight):
        self._genes = []
        self._maxWeight = maxWeight
        self._weight = 0
        self._value = 0

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, genes):
        self._genes = genes

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def GenesToItems(self):
        i = 0
        items = []
        while (len(self._genes) > i):
            items.append(self._genes[i].id)
            i += 1
        return items

    def ShowMeYourGenes(self):
        genesId = '[ '
        i = 0
        while (len(self._genes) > i):
            genesId = genesId + str(self._genes[i].id) + ' '
            i += 1
        genesId = genesId + ']'
        print(f'weight = {self._weight} value = {self._value} {genesId}')

    def Born(self, genes):
        minWeightGenes = genes[0].weight
        minWeightIter = 0
        geneAvailability = [1] * len(genes)
        probability = 1/len(genes)
        while ((self._maxWeight - self._weight) >= minWeightGenes):
            i = int(random.random()/probability)
            if ((geneAvailability[i] == 1) & ((self._maxWeight - self._weight) >= genes[i].weight)):
                geneAvailability[i] = 0
                self._genes.append(genes[i])
                self._weight += genes[i].weight
                self._value += genes[i].value
                if (i == minWeightIter):
                    geneAvailability[minWeightIter] = 0
                    minWeightIter = next((j for j, x in enumerate(geneAvailability) if x), None)
                    if(minWeightIter != None):
                        minWeightGenes = genes[minWeightIter].weight
                    else:
                        break
        return self
