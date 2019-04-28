# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:31:44 2019

https://programmers.co.kr/learn/courses/30/lessons/49994
"""

dirs = 'ULURRDLLU'
dirs = 'LULLLLLLU'

#%%
def visit_length(dirs) :
    last = (0,0)
    mypath = []
    
    for dir in dirs :
        
        if dir == 'U' :
            current = (last[0], last[1]+1)
        elif dir == 'D' : 
             current = (last[0], last[1]-1)
        elif dir == 'L' :
            current = (last[0]-1, last[1])
        elif dir == 'R' :
            current = (last[0]+1, last[1])
        
        if (current[0] <=5) and (current[0] >= -5) and (current[1] <=5) and (current[1]  >= -5) :
            
            if [last, current] not in mypath :
                mypath.append([last, current])
                
            if [current, last] not in mypath :
                mypath.append([current, last])
                
            last = current
            
        else :
            current = last
            
    answer = len(mypath)//2
    return answer
