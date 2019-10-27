# -*- coding: utf-8 -*-
"""
https://www.acmicpc.net/problem/14502

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
0->빈 칸 / 1->벽 / 2->바이러스
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.

추가될 1의 개수 반드시 세개. 안전 영역 최댓값을 구하시오.
2<= 바이러스 수 <=10

7 7
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
mymap = [list(map(int, input().split(' '))) for _ in range(N)]

#%%
#좌표
virus = [[x, y] for x, li in enumerate(mymap) for y, val in enumerate(li) if val==2]
nothing = [[x, y] for x, li in enumerate(mymap) for y, val in enumerate(li) if val==0]
#%%
def virus_spread(virus, wall_map) :
    
    visiting = virus.copy()
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while visiting :
        x, y = visiting.pop(0)
    
        for i in range(4) :
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            
            if temp_x >= 0 and temp_x < N and temp_y >= 0 and temp_y < M :
                if wall_map[temp_x][temp_y] == 0 and mymap[temp_x][temp_y] == 0 :
                    wall_map[temp_x][temp_y] = 2
                    visiting.append([temp_x, temp_y])
    #0의 개수 return                
    return sum([mm.count(0) for mm in wall_map])

#%%

from itertools import combinations
combi_list = list(combinations(nothing, 3))
answer_list = []

#%%
for combi in combi_list :
    wall_map = [mm[:] for mm in mymap]
    
    for val in combi :
        wall_map[val[0]][val[1]] = 1
    answer_list.append(virus_spread(virus, wall_map))

#%%
print(max(answer_list))
