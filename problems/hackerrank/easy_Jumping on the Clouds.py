# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:12:29 2019

https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

n = 7
c = [0 ,0 ,1 ,0 ,0 ,1 ,0]
#%%
i = 0; cnt = 0
while i < n-1 :
    if i + 2 <= n-1 :
        if c[i + 2] == 0 :
            cnt += 1
            i += 2
        else :
            cnt += 1
            i += 1
            
    elif i + 1 <= n-1 :
        cnt += 1
        i += 1
        