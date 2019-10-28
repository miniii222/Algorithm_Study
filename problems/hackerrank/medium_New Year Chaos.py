# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:16:21 2019
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
"""

n =5
q = [2,5,1,3,4]
#q = [2,1,5,3,4]

#%%
def minimumBribes(q) :
    cnt_q = [[] * n for _ in range(n)]
    i = 0; cnt = 0
    while i < n-1 :
        if q[i] > q[i+1] :
    
            cnt_q[q[i] - 1].append(q[i+1])
            if len(set(cnt_q[q[i] - 1])) > 2 :
                return 'Too chaotic'
                break
            
            q[i], q[i+1] = q[i+1], q[i]
            
            cnt += 1
            if i-1 < 0 :
                i = 0
            else :
                i-= 1

        else :
            i += 1      
    return cnt
