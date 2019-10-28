# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:03:53 2019
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

n = 8
s = 'UDDDUDUU'
#%%
direction = [ss for ss in s]
dir_dict = {'U' : 1, 'D' : -1}
#%%
dir_list = []
for dd in direction :
    dir_list.append(dir_dict[dd])
#%%
from itertools import accumulate
dir_list = list(accumulate(dir_list))
#%%
cnt = 0
for i, dd in enumerate(dir_list) :
    if i == 0 and dd <0 :
        cnt += 1
    elif i > 0 and dir_list[i-1] >= 0 and dd < 0 :
        cnt += 1
