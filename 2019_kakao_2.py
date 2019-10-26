# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:53:02 2019

@author: Seungmini
"""

#https://programmers.co.kr/learn/courses/30/lessons/42889
#%%
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

N = 4
stages = [4,4,4,4,4]
#%%
def solution(N, stages):
    prob = [0] * N
    for i in range(1, N+1) :
        try :
            prob[i-1] = len([ss for ss in stages if ss == i]) / len([ss for ss in stages if ss >= i])
        except :
            pass
    number = list(range(1, N+1))
    temp = sorted(zip(prob, number), key = lambda x : x[0], reverse = True)

    a,b = map(list, zip(*temp))
    return b