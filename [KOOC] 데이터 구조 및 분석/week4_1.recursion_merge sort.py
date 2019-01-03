# -*- coding: utf-8 -*-
import random
#%%
def performMergeSort(lstElementToSort) :
    if len(lstElementToSort) == 1 :
        return lstElementToSort
    
    #Decomposition
    lstSubElementToSort1 = []
    lstSubElementToSort2 = []
    
    for itr in range(len(lstElementToSort)) :
        if len(lstElementToSort)/2 > itr :
            lstSubElementToSort1.append(lstElementToSort[itr])
        else :
            lstSubElementToSort2.append(lstElementToSort[itr])
    
    #Recursion : sorted    
    lstSubElementToSort1 = performMergeSort(lstSubElementToSort1)
    lstSubElementToSort2 = performMergeSort(lstSubElementToSort2)
    
    #Aggregation
    idxCount1 =0 ; idxCount2 =0
    
    for itr in range(len(lstElementToSort)) :
        if idxCount1 == len(lstSubElementToSort1) :
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 += 1
            
        elif idxCount2 == len(lstSubElementToSort2) :
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 += 1
            
        elif lstSubElementToSort1[idxCount1] > lstSubElementToSort2[idxCount2] :
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 += 1
            
        else :
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 += 1
            
    return lstElementToSort

#%%
lstRandom = []
for i in range(10) :
    lstRandom.append(random.randrange(0,100))
print(lstRandom)

performMergeSort(lstRandom)
