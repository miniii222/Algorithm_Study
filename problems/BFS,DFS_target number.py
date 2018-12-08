# -*- coding: utf-8 -*-
"""

@author: Seungmini
"""
#https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
numbers = [1,1,1,1,1]
target = 5
#%%
def target_num_DFS(numbers, target):
    answer = 0; n = len(numbers)
    
    for sign in [1,-1] :
        stack = [[sign]]
        while stack:
            path = stack.pop()
            
            if len(path)== n:                
                mynum = [path[i]*numbers[i] for i in range(n)]
                if sum(mynum) == target : #값이 맞으면
                    answer +=1    
            else:
                for m in [1,-1]:
                    stack.append(path + [m])
    return answer

#%%
import time

numbers = [1,1,1,1,1,1,2,5,7,8,6,5,4,2,1,1,1,1]; target = 49 
numbers = [1,1,1,1,1];target = 5
#%%
start_time = time.time()
target_num_DFS(numbers, target)
print("DFS 소요시간" , time.time()- start_time)

