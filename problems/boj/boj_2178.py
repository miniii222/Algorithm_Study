# -*- coding: utf-8 -*-
"""
https://www.acmicpc.net/problem/2178

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.

추가될 1의 개수 반드시 세개. 안전 영역 최댓값을 구하시오.
2<= 바이러스 수 <=10
"""
N = 7; M = 7
my = [None]*N

"""
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""
NM = input().split(' ')
NM = list(map(int, NM))
N=NM[0]; M = NM[1]; mymap = [None]*N

for i in range(N) :
    mymap[i] = list(input())
    mymap[i] = list(map(int, mymap[i]))

start = [0,0]
end = [N-1,M-1]

#[i][j] up : [i-1][j] / down : [i+1][j] / left : [i][j-1] / right : [i][j+1]

#%%
path = []
def DFS_path(start, end, visited = []) :
    direction = []
    visited = visited + [start]
    up = [start[0]-1,start[1]] ; down = [start[0]+1,start[1]]; left = [start[0],start[1]-1]; right = [start[0],start[1]+1]
    
    if start == end :
        path.append(visited)
    
    if up[0] >=0 :
        direction.append(up)
    if down[0] <=(N-1) :
        direction.append(down)
    if left[1] >=0 :
        direction.append(left)
    if right[1] <=(M-1) :
        direction.append(right)
    
    for child in direction :
        if mymap[child[0]][child[1]] ==1  and child not in visited :
            DFS_path(child,end, visited)

DFS_path(start, end)

min_path = []
for i in range(len(path)) :
    min_path.append(len(path[i]))
    
print(min(min_path))

#시간초과 ㅜㅜ
               
#%%
paths = []
def BFS_path(start, end, visited=[]):
    
    visited = visited + [start]
    direction = []
        
    if start == end:
        paths.append(visited)
    
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        up = [vertex[0]-1,vertex[1]] ; down = [vertex[0]+1,vertex[1]]; left = [vertex[0],vertex[1]-1]; right = [vertex[0],vertex[1]+1]
        
        if up[0] >=0 :
            direction.append(up)
        if down[0] <=(N-1) :
            direction.append(down)
        if left[1] >=0 :
            direction.append(left)
        if right[1] <=(M-1) :
            direction.append(right)
            
        for node in direction:
            if mymap[node[0]][node[1]] ==1 and node not in visited:
                BFS_path(node, end, visited)
                
#%%
BFS_path(start, end)

min_path = []
for i in range(len(paths)) :
    min_path.append(len(paths[i]))
    
print(min(min_path))
#시간초과 ㅜㅜ

#%%
paths = []
def BFS_path(start, end, visited=[]):
    
    direction = []
    
    queue = [start]
    
    while queue:
        a,b = queue.pop(0)
        visited.append([a,b])
        
        if a==end[0] and b== end[1] :
            paths.append(visited)
            break

        up = [a-1,b] ; down = [a+1,b]; left = [a,b-1]; right = [a,b+1]
        
        if up[0] >=0 :
            direction.append(up)
        if down[0] <=(N-1) :
            direction.append(down)
        if left[1] >=0 :
            direction.append(left)
        if right[1] <=(M-1) :
            direction.append(right)
            
        for node in direction:
            if mymap[node[0]][node[1]] ==1 and node not in visited:
                queue.append([node[0], node[1]])
#%%
BFS_path(start, end)
paths
