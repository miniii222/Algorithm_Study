# -*- coding: utf-8 -*-
"""
https://www.acmicpc.net/problem/2798

5 21
5 6 7 8 9

5 15
1 2 3 4 5
"""

NM = list(map(int, input().split(' ')))
N=NM[0]; M = NM[1]

cards = list(map(int, input().split(' ')))

from itertools import combinations
cards = list(combinations(cards, 3))
#%%

flag = 0
answer = []
for card in cards :
    ss = sum(card)
    if ss == M :
        print(ss)
        flag = 1
        break
        
    elif M > ss :
        answer.append(ss)
        
if flag == 0 :
    print(max(answer))