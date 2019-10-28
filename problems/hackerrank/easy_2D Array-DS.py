# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:23:00 2019

https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
arr = [[-9, -9, -9,  1, 1, 1], 
 [0, -9,  0,  4, 3, 2],
[-9, -9, -9,  1, 2, 3],
 [0,  0,  8,  6, 6, 0],
 [0,  0,  0, -2, 0, 0],
 [0,  0,  1,  2, 4, 0]]
#%%
dx = [-1,1,-1,-1,1,1,0]
dy = [0,0,-1,1,-1,1,0]
#%%
def hourglassSum(arr) :
    arr1 = []
    n = len(arr)
    for i in range(1,n-1) :
        for j in range(1,n-1) :
            x = i; y = j
            sum1 = 0
            for dd in range(7) :
                sum1 += arr[x + dx[dd]][y + dy[dd]]
            arr1.append(sum1)
        
    return max(arr1)

#%%
hourglassSum(arr)