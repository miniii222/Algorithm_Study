# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 13:19:19 2018

@author: Seungmini
"""
#https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
numbers = [1,1,1,1,1]
target = 3
#%%
def target_num_BFS(numbers, target):
    answer = 0; numbers = list(map(str, numbers)); n = len(numbers)
    for sign in ['+','-'] :
        queue = [[sign]]
                
        while queue:
            path = queue.pop(0)
            
            if len(path)==n:                
                mynum = [None]*(2*n)
                for i in range(2*n) :
                   if i%2 ==0 :
                       mynum[i] = path[i//2]
                   else :
                       mynum[i] = numbers[i//2]
                str1 = ''.join(mynum)
                if eval(str1) == target :
                    answer +=1    
            else:
                for m in ['+','-']:
                    queue.append(path + [m])
        
    
    return answer
#%%
target_num_BFS(numbers, target)      

#for구문을 돌리면서 조건에 맞는 것만 가져오는 것이 빠를까? 다 가져와서 조건에 맞는 것만 추출하는 것이 빠를까?