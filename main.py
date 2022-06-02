# 4.Реализовать муравьиный алгоритм.

import pandas as pd
from BruteForceMethod import *
from EvolutionAlgorithm import *
from AntAlgotithm import *
import random

MAXWEIGHTKNAPSACK = 30
COUNTFIRSTGENERATION = 100000
COUNTITERATIONFOREVOLUTION = 100
COUNTSELECTION = 0.52
COUNTREPRODUCTION = 0.9
COUNTMUTATION = 0.1
WEIGHTTOP = 20
WEIGHTBOT = 1
VALUETOP = 50
VALUEBOT = 1
COUNTANTS = 5000
COUNTITERATIONFORANTS = 30
EVAPORATIONCOEFFICIENT = 0.08
FLAGEVOLUTION = False
FLAGANTS = True

def SortingItems(items):
    i = 0
    j = 1
    while i < (len(items[0]) - 1):
        mini = i
        while j < (len(items[0])):
            if ((items[0][j] == items[0][mini]) & (items[1][j] > items[1][mini])):
                mini = j
            if items[0][j] < items[0][mini]:
                mini = j
            j += 1
        if mini != i:
            a = items[0][i]
            items[0][i] = items[0][mini]
            items[0][mini] = a
            a = items[1][i]
            items[1][i] = items[1][mini]
            items[1][mini] = a
            a = items[2][i]
            items[2][i] = items[2][mini]
            items[2][mini] = a
        i += 1
        j = i + 1
    return items


def MakingItems(weightTop, weightBot, valueTop, valueBot, countIems):
    itemsID = []
    itemsWeight = []
    itemsValue = []
    itemsNewID = []
    i = 0
    while (i < countIems):
        itemsWeight.append(random.randint(weightBot, weightTop))
        itemsValue.append(random.randint(valueBot, valueTop))
        itemsNewID.append(i)
        i += 1
    items = [itemsWeight, itemsValue, itemsNewID]
    # print(items)
    return items


if __name__ == '__main__':
    items = [[1, 3, 4, 4, 5, 5, 6, 7, 8, 10, 12, 17],
             [6, 2, 4, 10, 5, 17, 13, 9, 7, 16, 25, 33],
             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    # itemsf = pd.DataFrame([[12, 25], [7, 9], [5, 17], [6, 13], [10, 16], [3, 2],
    #                       [5, 5], [1, 6], [17, 33], [4, 4], [4, 10], [8, 7]],
    #                      columns=['weight', 'value'])
    # items = itemsf.tolist()
    # print(itemsf.loc[4, 'value'])
    # items = SortingItems(items)
    print(items)
    # new50Items = MakingItems(WEIGHTTOP, WEIGHTBOT, VALUETOP, VALUEBOT, 50)
    # new100Items = MakingItems(WEIGHTTOP, WEIGHTBOT, VALUETOP, VALUEBOT, 100)
    # new500Items = MakingItems(WEIGHTTOP, WEIGHTBOT, VALUETOP, VALUEBOT, 500)
    # new500Items = [new500Items_df['weight'].tolist(), new500Items_df['value'].tolist(), new500Items_df.index.values.tolist()]

    # new50Items_df = pd.read_excel('src/50_new_items.xlsx', engine='openpyxl', index_col=0)
    # new100Items_df = pd.read_excel('src/100_new_items.xlsx', engine='openpyxl', index_col=0)
    # new500Items_df = pd.read_excel('src/500_new_items.xlsx', engine='openpyxl', index_col=0)

    # print(new50Items_df)
    # print(new100Items_df)
    # print(new500Items_df)

    # new50Items = SortingItems(new50Items)
    # new100Items = SortingItems(new100Items)
    # new500Items = SortingItems(new500Items)
    #
    # new50Items_d = {'weight': new50Items[0], 'value': new50Items[1], 'originalID': new50Items[2]}
    # new50Items_df = pd.DataFrame(new50Items_d)
    # new50Items_df.to_excel('src/50_new_items.xlsx', sheet_name='50_items')
    #
    # new100Items_d = {'weight': new100Items[0], 'value': new100Items[1], 'originalID': new100Items[2]}
    # new100Items_df = pd.DataFrame(new100Items_d)
    # new100Items_df.to_excel('src/100_new_items.xlsx', sheet_name='100_items')
    #
    # new500Items_d = {'weight': new500Items[0], 'value': new500Items[1], 'originalID': new500Items[2]}
    # new500Items_df = pd.DataFrame(new500Items_d)
    # new500Items_df.to_excel('src/500_new_items.xlsx', sheet_name='500_items')
    #
    new50Items_df = pd.read_excel('src/50_new_items.xlsx', engine='openpyxl', index_col=0)
    new100Items_df = pd.read_excel('src/100_new_items.xlsx', engine='openpyxl', index_col=0)
    new500Items_df = pd.read_excel('src/500_new_items.xlsx', engine='openpyxl', index_col=0)

    new50Items = [new50Items_df['weight'].to_list(), new50Items_df['value'].to_list(),
                  new50Items_df['originalID'].to_list()]
    new100Items = [new100Items_df['weight'].to_list(), new100Items_df['value'].to_list(),
                   new100Items_df['originalID'].to_list()]
    new500Items = [new500Items_df['weight'].to_list(), new500Items_df['value'].to_list(),
                   new500Items_df['originalID'].to_list()]

    print(new50Items)
    print(new100Items)
    print(new500Items)

    items_result = []
    items_result_50 = []
    items_result_100 = []
    items_result_500 = []

    if (FLAGEVOLUTION):
        i = 0
        while (i < 5):
            # items_result.append(EvolutionAlgorithm(COUNTFIRSTGENERATION, COUNTITERATIONFOREVOLUTION, COUNTSELECTION, COUNTREPRODUCTION,
            #                                        COUNTMUTATION, items, MAXWEIGHTKNAPSACK).TheEvolutionBegins())
            items_result_50.append(
                EvolutionAlgorithm(COUNTFIRSTGENERATION, COUNTITERATIONFOREVOLUTION, COUNTSELECTION, COUNTREPRODUCTION,
                                   COUNTMUTATION, new50Items, MAXWEIGHTKNAPSACK).TheEvolutionBegins())
            items_result_100.append(
                EvolutionAlgorithm(COUNTFIRSTGENERATION, COUNTITERATIONFOREVOLUTION, COUNTSELECTION, COUNTREPRODUCTION,
                                   COUNTMUTATION, new100Items, MAXWEIGHTKNAPSACK).TheEvolutionBegins())
            items_result_500.append(
                EvolutionAlgorithm(COUNTFIRSTGENERATION, COUNTITERATIONFOREVOLUTION, COUNTSELECTION, COUNTREPRODUCTION,
                                   COUNTMUTATION, new500Items, MAXWEIGHTKNAPSACK).TheEvolutionBegins())
            i += 1

        print(items_result_50)
        print(items_result_100)
        print(items_result_500)

        weight = []
        value = []
        items = []
        i = 0
        while (i < len(items_result_50)):
            weight.append(items_result_50[i][0])
            value.append(items_result_50[i][1])
            items.append(items_result_50[i][2])
            i += 1
        new50Items_df = pd.DataFrame(
            {'weight': weight, 'value': value, 'item_ID': items})
        new50Items_df.to_excel('src/evolution_50_items_result.xlsx', sheet_name='50_items')

        weight = []
        value = []
        items = []
        i = 0
        while (i < len(items_result_100)):
            weight.append(items_result_100[i][0])
            value.append(items_result_100[i][1])
            items.append(items_result_100[i][2])
            i += 1
        new100Items_df = pd.DataFrame(
            {'weight': weight, 'value': value, 'item_ID': items})
        new100Items_df.to_excel('src/evolution_100_items_result.xlsx', sheet_name='100_items')

        weight = []
        value = []
        items = []
        i = 0
        while (i < len(items_result_500)):
            weight.append(items_result_500[i][0])
            value.append(items_result_500[i][1])
            items.append(items_result_500[i][2])
            i += 1
        new500Items_df = pd.DataFrame(
            {'weight': weight, 'value': value, 'item_ID': items})
        new500Items_df.to_excel('src/evolution_500_items_result.xlsx', sheet_name='500_items')

    items_result = []
    items_result_50 = []
    items_result_100 = []
    items_result_500 = []

    if (FLAGANTS):
        i = 0
        while (i < 5):
            # items_result.append(AntAlgorithm(COUNTANTS, COUNTITERATIONFORANTS, MAXWEIGHTKNAPSACK, items, EVAPORATIONCOEFFICIENT).BonAppetit())
            items_result_50.append(
                AntAlgorithm(COUNTANTS, COUNTITERATIONFORANTS, MAXWEIGHTKNAPSACK, new50Items, EVAPORATIONCOEFFICIENT).BonAppetit())
            items_result_100.append(
                AntAlgorithm(COUNTANTS, COUNTITERATIONFORANTS, MAXWEIGHTKNAPSACK, new100Items, EVAPORATIONCOEFFICIENT).BonAppetit())
            items_result_500.append(
                AntAlgorithm(COUNTANTS, COUNTITERATIONFORANTS, MAXWEIGHTKNAPSACK, new500Items, EVAPORATIONCOEFFICIENT).BonAppetit())
            i += 1
        print(items_result_50)
        print(items_result_100)
        print(items_result_500)

        weight = []
        value = []
        items = []
        i = 0
        while (i < len(items_result_50)):
            weight.append(items_result_50[i][0])
            value.append(items_result_50[i][1])
            items.append(items_result_50[i][2])
            i += 1
        new50Items_df = pd.DataFrame(
            {'weight': weight, 'value': value, 'item_ID': items})
        new50Items_df.to_excel('src/ants_50_items_result.xlsx', sheet_name='50_items')

        weight = []
        value = []
        items = []
        i = 0
        while (i < len(items_result_100)):
            weight.append(items_result_100[i][0])
            value.append(items_result_100[i][1])
            items.append(items_result_100[i][2])
            i += 1
        new100Items_df = pd.DataFrame(
            {'weight': weight, 'value': value, 'item_ID': items})
        new100Items_df.to_excel('src/ants_100_items_result.xlsx', sheet_name='100_items')

        weight = []
        value = []
        items = []
        i = 0
        while (i < len(items_result_500)):
            weight.append(items_result_500[i][0])
            value.append(items_result_500[i][1])
            items.append(items_result_500[i][2])
            i += 1
        new500Items_df = pd.DataFrame(
            {'weight': weight, 'value': value, 'item_ID': items})
        new500Items_df.to_excel('src/ants_500_items_result.xlsx', sheet_name='500_items')

    print(AntAlgorithm(COUNTANTS, COUNTITERATIONFORANTS, MAXWEIGHTKNAPSACK, items, EVAPORATIONCOEFFICIENT).BonAppetit())
