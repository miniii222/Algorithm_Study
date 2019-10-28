# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:47:02 2019
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
arr = [1, 3, 5, 2, 4, 6, 7]
arr = [4,3,1,2]
n = len(arr)
arr
#%%시간초과 ㅎㅎ
cnt = 0
for i in range(1, n+1) :
    print(i)
    arr_ind = arr.index(i)
    if arr_ind != i-1 :
        arr[arr_ind], arr[i-1] = arr[i-1], arr[arr_ind]
        print(arr)
        cnt += 1
        
#%%시간초과 ㅎㅎ
cnt = 0
for i in range(n) :
    if arr[i] != i+1 :
        arr_ind = arr.index(i+1)
        arr[arr_ind], arr[i] = arr[i], arr[arr_ind]
        cnt += 1