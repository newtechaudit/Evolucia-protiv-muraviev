import pandas as pd
import numpy as np

# Constants A and B for function RankingSel
A = 1.2
B = 2.0 - 1.2
# Constant MU for function UniRankingSel
MU = 1.0
DEFAULTTYPESELECTION = 1
DEFAULTTYPEREPRODUCTION = 1
DEFAULTTYPEMUTATION = 1
from Genotype import *

def SortingGenes(genes):
    i = 0
    j = 1
    while i < (len(genes)-1):
        mini = i
        while j < (len(genes)):
            if genes[j].weight < genes[mini].weight:
                mini = j
            j+=1
        if mini != i:
            a = genes[i]
            genes[i] = genes[mini]
            genes[mini] = a
        i+=1
        j = i+1
        #print(items)
    return genes

def SortingByFitness(population):
    i = 0
    j = 1
    while i < (len(population) - 1):
        maxi = i
        while j < (len(population)):
            if population[j].value > population[maxi].value:
                maxi = j
            j += 1
        if maxi != i:
            a = population[i]
            population[i] = population[maxi]
            population[maxi] = a
        i += 1
        j = i + 1
        k = 0
        #while len(population) > k:
        #    population[k].ShowMeYourGenes
        #    k+=1
    return population

class EvolutionAlgorithm:
    def __init__(self, countFirstGeneration, countIteration, countSelection, countReproduction, countMutation, items, maxGenotypeWeight):
        self._countFirstGeneration = countFirstGeneration
        self._countIteration = countIteration
        self._countSelection = countSelection
        self._countReproduction = countReproduction
        self._countMutation = countMutation
        self._items = items
        self._maxGenotypeWeight = maxGenotypeWeight
        self._genes = []

    @property
    def countFirstGeneration(self):
        return self._countFirstGeneration

    @countFirstGeneration.setter
    def countFirstGeneration(self, countFirstGeneration):
        self._countFirstGeneration = countFirstGeneration

    @property
    def countIteration(self):
        return self._countIteration

    @countIteration.setter
    def countIteration(self, countIteration):
        self._countIteration = countIteration

    @property
    def countSelection(self):
        return self._countSelection

    @countSelection.setter
    def countSelection(self, countSelection):
        self._countSelection = countSelection

    @property
    def countReproduction(self):
        return self._countReproduction

    @countReproduction.setter
    def countReproduction(self, countReproduction):
        self._countReproduction = countReproduction

    @property
    def countMutation(self):
        return self._countMutation

    @countMutation.setter
    def countMutation(self, countMutation):
        self._countMutation = countMutation

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def genes(self):
        return self._genes

    @genes.setter
    def genes(self, genes):
        self._genes = genes

#Selection

    def TournamentSel(self, population, countAlive):
        newPopulation = []
        genotypeAvailability = [1] * len(population)
        probability = 1/len(population)
        i = 0
        while (i < countAlive):
            first = int(random.random() / probability)
            second = int(random.random() / probability)
            if ((first != second)&(genotypeAvailability[first] == 1)&(genotypeAvailability[second] == 1)):
                if (population[first].value >= population[second].value):
                    genotypeAvailability[first] = 0
                    newPopulation.append(population[first])
                if (population[first].value < population[second].value):
                    genotypeAvailability[second] = 0
                    newPopulation.append(population[second])
                i += 1
        return newPopulation

    def RouletteSel(self, population, countAlive):
        newPopulation = []
        i = 0
        fitnessSum = 0
        genotypeProbability = []
        while (i < len(population)):
            fitnessSum += population[i].value
            i += 1
        genotypeProbability.append(population[0].value / fitnessSum)
        i = 1
        while (i < len(population)):
            genotypeProbability.append(genotypeProbability[i-1] + (population[i].value / fitnessSum))
            i += 1
        genotypeAvailability = [1] * len(population)
        i = 0
        while (i < (countAlive)):
            j = random.random()
            z = 0
            while (z < (len(population))):
                if ((genotypeProbability[z] >= j) & (genotypeAvailability[z] == 0)):
                    break
                if ((genotypeProbability[z] >= j)&(genotypeAvailability[z] == 1)):
                    genotypeAvailability[z] = 0
                    newPopulation.append(population[z])
                    i += 1
                    break
                z += 1
        i = 0
        return newPopulation

    def RankingSel(self, population, countAlive):
        newPopulation = []
        population = SortingByFitness(population)
        genotypeProbability = []
        genotypeProbability.append(1 / len(population) * (A - ((A - B) * (1 - 1) / (len(population) - 1))))
        i = 2
        while (i < (len(population)+1)):
            probability = 1 / len(population) * (A - ((A - B) * (i - 1) / (len(population) - 1)))
            genotypeProbability.append(genotypeProbability[i-2] + probability)
            i += 1
        genotypeAvailability = [1] * len(population)
        i = 0
        while (i < (countAlive)):
            j = random.random()
            z = 0
            while (z < (len(population))):
                if ((genotypeProbability[z] >= j) & (genotypeAvailability[z] == 0)):
                    break
                if ((genotypeProbability[z] >= j) & (genotypeAvailability[z] == 1)):
                    genotypeAvailability[z] = 0
                    newPopulation.append(population[z])
                    i += 1
                    break
                z += 1
        return newPopulation

    def UniRankingSel(self, population, countAlive):
        newPopulation = []
        population = SortingByFitness(population)
        genotypeAvailability = [1] * (len(population) * MU)
        probability = 1 / (len(population) * MU)
        i = 0
        while (i < countAlive):
            first = int(random.random() / probability)
            if ((genotypeAvailability[first] == 1)):
                genotypeAvailability[first] = 0
                newPopulation.append(population[first])
                i += 1
        return newPopulation

#Reproduction

    def PanmixiaRep(self, population, parentAvailability, countChildren):
        i = 0
        parentProbability = []
        probability = 1 / len(population)
        for i in parentProbability:
            i = probability * (i + 1)
        while (i < countChildren):
            firstParent = int(random.random()/probability)
            #print(f'First {firstParent}')
            if ((parentAvailability[firstParent] == 1)):
                secondParent = int(random.random() / probability)
                #print(f'Second {secondParent}')
                if((firstParent != secondParent)):
                    #print(f'\n{i}\n')
                    j = 0
                    parentsGenes = []
                    while (j < len(population[firstParent].genes)):
                        parentsGenes.append(population[firstParent].genes[j])
                        j += 1
                    j = 0
                    while (j < len(population[secondParent].genes)):
                        parentsGenes.append(population[secondParent].genes[j])
                        j += 1
                    parentsGenes = list(set(parentsGenes))
                    #population[firstParent].ShowMeYourGenes()
                    #population[secondParent].ShowMeYourGenes()
                    parentsGenes = SortingGenes(parentsGenes)
                    #j = 0
                    #while (j < len(parentsGenes)):
                    #    Gene.ShowTheGene(parentsGenes[j])
                    #    j += 1
                    population.append(Genotype(self._maxGenotypeWeight).Born(parentsGenes))
                    i += 1
        return population

    def InbreedingRep(self, population):
        return population

    def OutbreedingRep(self, population):
        return population

# Mutation

    def RandomMut(self, population, countMutant):
        i = 0
        while (i < countMutant):
            population.append(Genotype(self._maxGenotypeWeight).Born(self._genes))
            i += 1
        return population

    def RareGenesMut(self, population, countMutant):
        return population

#Algorithm

    def TheEvolutionBegins(self):
        self._genes = TransformationGenes(self._items)
        population = []
        while (len(population) < self._countFirstGeneration):
            population.append(Genotype(self._maxGenotypeWeight).Born(self._genes))
        # i = 0
        # while (i < len(population)):
        #     Genotype.ShowMeYourGenes(population[i])
        #     i += 1

        # print("Choose the method of selection\n1.Tournament\n2.Method of roulette"
        #     "\n3.Ranking\n4.Uniform ranking")
        # typeSelection = int(input())
        # print("Choose the method of reproduction\n1.Panmixia\n2.Inbreeding"
        #     "\n3.Outbreeding")
        # typeReproduction = int(input())
        # print("Choose the method of mutation\n1.Random\n2.Rare Genes")
        # typeMutation = int(input())
        typeSelection = DEFAULTTYPESELECTION
        typeReproduction = DEFAULTTYPEREPRODUCTION
        typeMutation = DEFAULTTYPEMUTATION
        i = 0
        while ((i < (self._countIteration)) & (len(population) > 1)):

            countAlive = int(len(population) * self._countSelection)
            if typeSelection == 1:
                population = EvolutionAlgorithm.TournamentSel(self, population, countAlive)
            if typeSelection == 2:
                population = EvolutionAlgorithm.RouletteSel(self, population, countAlive)
            if typeSelection == 3:
                population = EvolutionAlgorithm.RankingSel(self, population, countAlive)
            if typeSelection == 4:
                population = EvolutionAlgorithm.UniRankingSel(self, population, countAlive)

            parentAvailability = [1] * len(population)
            countChildren = int(self._countReproduction * len(population) / 2)
            if typeReproduction == 1:
                population = EvolutionAlgorithm.PanmixiaRep(self, population, parentAvailability, countChildren)
            if typeReproduction == 2:
                population = EvolutionAlgorithm.InbreedingRep(self, population, parentAvailability, countChildren)
            if typeReproduction == 3:
                population = EvolutionAlgorithm.OutbreedingRep(self, population, parentAvailability, countChildren)

            countMutant = int(self._countMutation * len(population))
            if typeMutation == 1:
                population = EvolutionAlgorithm.RandomMut(self, population, countMutant)
            if typeMutation == 2:
                population = EvolutionAlgorithm.RareGenesMut(self, population, countMutant)

            # print(i)


            i += 1
            print(i)
        j = 0
        while (j < len(population)):
            Genotype.ShowMeYourGenes(population[j])
            j += 1
        # Genotype.ShowMeYourGenes(population[0])
        print(i)
        result = [population[0].weight, population[0].value, population[0].GenesToItems()]
        return result