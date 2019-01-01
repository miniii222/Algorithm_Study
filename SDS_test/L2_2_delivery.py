# -*- coding: utf-8 -*-
2
7 7 3 7
6 4 1
1 2
2 3
4 1
4 3
7 5
5 3
5 6
#%%input
#T = int(input())
NMKS = input().split(' ')
NMKS = list(map(int, NMKS))
N = NMKS[0]; M = NMKS[1]; K = NMKS[2]; S = NMKS[3] #N = 마을 수, M = 도로 수, K = 배달해야 하는 마을 개수, S = 시작 마을

#배달할 마을 번호
delivery = input().split(' ')
#delivery = delivery[:-1]
delivery = list(map(int, delivery))
#%%input에서 받아서 바로 dict만들기
road_dict = {}
keys = range(1,N+1)
for key in keys :
    road_dict[key] = []

for j in range(M) :
    ab = input().split(' ')
    ab = list(map(int, ab))
    road_dict[ab[0]].append(ab[1])
    road_dict[ab[1]].append(ab[0])
#%%    
def BFS_path(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            return len(path)-1
        
        else:
            for m in set(graph[n]) - set(path):
                queue.append((m, path + [m]))
#%%
BFS_path(road_dict, 7,6)
BFS_path(road_dict, 7,4)
BFS_path(road_dict, 7,1)

BFS_path(road_dict, 6,4)
BFS_path(road_dict, 6,1)
#%%
if K<=2 :
    answer = BFS_path(road_dict,S,delivery[0])+ sum([BFS_path(road_dict,delivery[i],delivery[i+1]) for i in range(K-1)])+BFS_path(road_dict,delivery[-1],S)
#%%Dijkstra's algorithm
delivery = [1,4,6]; path = 0
now_delivery = S    

while delivery :
    weight = [BFS_path(road_dict, now_delivery, dd) for dd in delivery]
    min_weight = min(weight)
    path += min_weight
    now_delivery = delivery.pop(weight.index(min_weight))
    
answer += BFS_path(road_dict,now_delivery,S)
#%%
#시작해서 배달을 마치고 돌아오는 마을과 가장 가까운 마을 두개를 우선 뽑겠다.
delivery.sort(key = lambda x : BFS_path(road_dict, S, x))
delivery[1],delivery[-1] = delivery[-1],delivery[1]



#%%뻘짓...
#road_matrix = [[0] * N]*N #연결 도로 정보 이렇게 하면 생성된 하나의 리스트 한개가 여러개가 생기는 효과. 하나만 바꿔도 바뀜 ㄷㄷ

road_matrix = [[0 for x in range(N)] for y in range(N)]

for i in range(M) :
    road=input().split(' ')
    road = list(map(int, road))
    
    road_matrix[road[0]-1][road[1]-1] = 1 #연결된 경우만 1로

road_matrix_t = list(map(list, zip(*road_matrix)))

road_sum = []
for road_row in range(N) :
    road_sum.append([first + second for first, second in zip(road_matrix[road_row], road_matrix_t[road_row])])
#%%
road_dict = {}

for j in range(N) :
    road_dict[j+1] = set([i+1 for i in range(N) if road_sum[j][i]==1])


#%%symmetric matrix multiplication
def matrixmulti (A):
    C = [[0 for x in range(N)] for y in range(N)]
    
    for j in range(N) :
        for i in range(N) :
            C[j][i] = sum( [a*b for a,b in zip(A[j], A[i]) ])
    
    return C
#%%
def find_route(start, end) :
    n=0
    if road_sum[start-1][end-1]>0 :
        n+=1
        
    else :
        n=2
        mymat = matrixmulti(road_sum)
        while mymat[start-1][end-1] <= 0 :
            mymat = matrixmulti(mymat)
            n+=1
            
    return n
#%%
answer = find_route(S,delivery[0])
for i in range(K-1):
    answer+=find_route(delivery[i],delivery[i+1])

answer += find_route(delivery[K-1],S)

#%%generate village
village = dict()

for j in range(N) :
    idx = [index+1 for index,value in enumerate(road_sum[j]) if value == 1]
    village[j+1] = idx
#%%

