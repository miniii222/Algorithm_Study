# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:40:30 2019

"""

#https://www.acmicpc.net/problem/2178
'''
4 6
101111
101010
101011
111011
'''
'''
2 25
1011101110111011101110111
1110111011101110111011101
'''

NM = input().split(' ')
NM = list(map(int, NM))
N=NM[0]; M = NM[1]
mymap = [None]*N 
#%%

for i in range(N) :
    mymap[i] = list(input())
    mymap[i] = list(map(int, mymap[i]))

start = [0,0]
end = [N-1,M-1]
#%%dfs(start, goal)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[0] * M for _ in range(N)] #지나간 경로 체크 및 구간 
#%%
visiting = [start]
while visiting :
    x, y = visiting.pop(0)
    
    if x == end[0] and y == end[1] :
        break
    
    for i in range(4) :
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        
        if temp_x >= 0 and temp_x < N and temp_y >= 0 and temp_y < M :
            if visited[temp_x][temp_y] == 0 and mymap[temp_x][temp_y] == 1 :
                visited[temp_x][temp_y] = visited[x][y] + 1
                visiting.append([temp_x, temp_y])
        
print(visited[x][y] + 1)
#%%
