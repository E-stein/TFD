import random
liste = [1635, 1655, 1688, 1711, 1733, 387, 657, 763, 873, 1471, 1001, 1515, 1657, 1855, 1980, 1292, 1377, 1427, 1458, 1506]
liste.sort()

def intervalle(k):
        listea = range(min(liste), min(liste) + 101)
        tada = set(liste).intersection(listea)
        global listek
        if len(tada) >= 2:
            listek = [range(min(liste), min(liste)+101)]
        else:
            listek = []
        
        return listek

for i in range(0, 18):
    k = liste.index(min(liste))
    intervalle(k)
    print(listek)
    liste.remove(min(liste))
    listek = listei
    print(listei)


print(liste1)
