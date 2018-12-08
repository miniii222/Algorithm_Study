# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:13:30 2018

@author: Seungmini
"""

h = [4,10,25,15,12,30,42,20,18,17]
n = len(h)

#i번째 노드의 부모 노드 위치 int((i-1)/2)
#i번째 노드의 왼쪽 자식 노드 위치 : 2*i+1
#i번째 노드의 오른쪽 자식 노드 위치 : 2*i+2
#트리의 높이 = int(log2(n))
#%%
def swap(list1,i,j) :
    list1[i], list1[j] = list1[j], list1[i]
#80
    
h = [4,14,7,2,8,1] 
#%% heapify (max-heap)

def heapify(unsorted) : #n:len(unsorted)
    
    i = 0 ; l = 2 * i+1; r = 2 * i+2
    n = len(unsorted)
    
    if unsorted[i] < unsorted[l] and l < n :
        swap(unsorted, l, i)
        
    if unsorted[i] < unsorted[r] and r < n :
        swap(unsorted, r, i)
        
    return(unsorted)
        

    
heapify(h)
#%% insertHeap
def insertHeap(element, list1) :
    #element 삽입할 숫자
    
    list2 = list1.copy()
    list2.append(element)
    
    if len(list2) == 1 :
        return(list2)
    
    i = len(list2)-1 #추가할 노드의 index
    j = int((i-1)/2) #i번쨰 노드의 부모노드 index
    
    while list2[j] > list2[i] : #부모 노드가 자식 노드보다 클 경우
        swap(list2,j,i)
        i = j
        j = int((i-1)/2)
        
    return list2

h2 = insertHeap(2,h)
h2

#%% deleteHeap
def deleteHeap(element, list1) :
    list2 = list1.copy()
    
    n = len(list2)
    
    #1.최솟값 제거
    if element == min(list2) :
        list2[0] = list2[n-1] #첫번째 노드로 마지막 노드보내기
        del list2[n-1] #마지막 노드 제거
        
        i = 0; l = 2*i+1; r = 2*i+2 #i 자기 index
                                    #l 왼쪽자식 index, r 오른쪽 자식 index
        
        while list2[i] > list2[l] or list2[i] > list2[r]:
            
            if list2[l] < list2[r] :
                j = l
            else :
                j = r
                
            swap(list2, i,j)
            
            i = j; l = 2*i+1; r = 2*i+2
            if l>=(n-1) or r>=(n-1) :
                
                return(list2)
                
    #2. 나머지
    
deleteHeap(4,h)
        
#2.나머지
